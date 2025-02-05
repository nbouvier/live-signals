"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from data_processing import create_figure, read_bin_file, process_file, create_multi_file_figure
from components.calculation_result import create_calculation_result
from components.fit_graph import create_fit_graph
from models import CalculationResult, FileData

def register_callbacks(app):
    """Register all callbacks for the application."""
    
    # Global variables to store data
    loaded_files = []  # List of FileData objects
    calculation_results = []
    
    @app.callback(
        [Output('strip-responses-graph', 'figure'),
         Output('strip-responses-graph', 'style'),
         Output('loaded-files-list', 'children'),
         Output('graph-placeholder', 'style'),
         Output('averages-content', 'children'),
         Output('fit-graph-container', 'children'),
         Output('strip-selection-panel', 'style')],
        Input('url', 'pathname')
    )
    def initialize_page(pathname):
        """Reset everything when the page loads."""
        # Clear all data
        loaded_files.clear()
        calculation_results.clear()
        CalculationResult.reset_id_counter()
        FileData.reset_id_counter()
        
        # Reset the display
        return (
            {},  # Empty figure
            dict(styles.BASE_GRAPH, **{'display': 'none'}),  # Hide graph
            None,  # Clear file info
            dict(styles.BASE_PLACEHOLDER, **{'display': 'block'}),  # Show upload placeholder
            None,  # Clear calculations
            None,  # Clear fit graph
            styles.OVERLAY  # Reset strip selection panel position
        )

    @app.callback(
        [Output('strip-responses-graph', 'figure', allow_duplicate=True),
         Output('strip-responses-graph', 'style', allow_duplicate=True),
         Output('loaded-files-list', 'children', allow_duplicate=True),
         Output('graph-placeholder', 'style', allow_duplicate=True)],
        [Input('upload-data', 'contents'),
         Input('add-file', 'contents'),
         Input({'type': 'time-offset', 'index': ALL}, 'value'),
         Input('strip-selector', 'value')],
        [State('upload-data', 'filename'),
         State('add-file', 'filename'),
         State({'type': 'time-offset', 'index': ALL}, 'id')],
        prevent_initial_call=True
    )
    def update_data(contents, add_contents, time_offsets, selected_strips, filename, add_filename, offset_ids):
        """Handle file upload and update the graph."""
        ctx_triggered = ctx.triggered_id
        
        if ctx_triggered == 'upload-data' and contents:
            # Clear existing data for initial upload
            loaded_files.clear()
            calculation_results.clear()
            CalculationResult.reset_id_counter()
            FileData.reset_id_counter()
            
            try:
                # Process the file
                file_data = process_file(contents, filename)
                loaded_files.append(file_data)
            except Exception as e:
                print(f"Error processing file: {e}")
                return dash.no_update, dash.no_update, dash.no_update, dash.no_update
                
        elif isinstance(ctx_triggered, dict) and ctx_triggered.get('type') == 'time-offset':
            # Update time offset for a file
            file_index = ctx_triggered['index']
            if file_index < len(loaded_files):
                try:
                    loaded_files[file_index].time_offset = float(time_offsets[file_index]) if time_offsets[file_index] else 0
                except ValueError:
                    pass
                    
        elif ctx_triggered == 'add-file' and add_contents:
            try:
                # Process and add new file
                file_data = process_file(add_contents, add_filename)
                loaded_files.append(file_data)
            except Exception as e:
                print(f"Error processing file: {e}")
                return dash.no_update, dash.no_update, dash.no_update, dash.no_update
        
        if not loaded_files:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update
            
        # Create file cards with time offset inputs
        file_cards = []
        for file_data in loaded_files:
            file_cards.append(html.Div([
                html.Div([
                    html.Span(f"File {file_data.id}", style={'color': styles.MUTED_TEXT_COLOR, 'fontSize': '12px', 'marginBottom': '4px'}),
                    html.Div([
                        html.I(className="fas fa-file-binary", style={'color': styles.MUTED_TEXT_COLOR}),
                        html.Span(file_data.filename)
                    ])
                ]),
                dcc.Input(
                    id={'type': 'time-offset', 'index': file_data.id},
                    type='number',
                    placeholder='Offset (ms)',
                    value=file_data.time_offset,
                    step=1,
                    style=styles.TIME_OFFSET_INPUT
                )
            ], style=styles.FILE_CARD))
        
        # Create figure with all files
        figure = create_multi_file_figure(loaded_files, selected_strips or [], calculation_results)
        
        return (
            figure,
            dict(styles.BASE_GRAPH, **{'display': 'block'}),
            file_cards,
            dict(styles.BASE_PLACEHOLDER, **{'display': 'none'})
        )

    @app.callback(
        [Output('averages-content', 'children', allow_duplicate=True),
         Output('popup-message', 'style'),
         Output('popup-message-content', 'children'),
         Output('close-popup', 'style'),
         Output('strip-responses-graph', 'figure', allow_duplicate=True)],
        [Input('calc-button', 'n_clicks')],
        [State('strip-selector', 'value'),
         State('strip-responses-graph', 'selectedData'),
         State('averages-content', 'children')],
        prevent_initial_call=True
    )
    def update_averages(n_clicks, selected_strips, selected_data, existing_content):
        if not n_clicks:  # Skip initial callback
            return None, {'display': 'none'}, None, {'display': 'none'}, dash.no_update

        try:
            # Get time range
            if selected_data and 'range' in selected_data:
                range_bounds = selected_data['range']['x']
            elif selected_data and 'points' in selected_data:
                x_values = [point['x'] for point in selected_data['points']]
                range_bounds = [min(x_values), max(x_values)]
            else:
                return (
                    existing_content,  # Keep existing content unchanged
                    styles.BASE_POPUP,
                    html.Div("Please make a selection first", style=styles.ERROR_MESSAGE),
                    styles.CLOSE_BUTTON,
                    dash.no_update
                )
                
            start_time, end_time = range_bounds
            
            # Calculate averages for each file
            all_strip_averages = []
            overall_averages = []
            
            for file_data in loaded_files:
                # Adjust time range for this file's offset
                adjusted_start = start_time - file_data.time_offset
                adjusted_end = end_time - file_data.time_offset
                
                # Find indices in the adjusted time range
                start_idx = np.searchsorted(file_data.time_values, adjusted_start)
                end_idx = np.searchsorted(file_data.time_values, adjusted_end)
                
                # Calculate strip averages for this file
                file_strip_averages = []
                for strip_num in selected_strips:
                    strip_avg = np.mean(file_data.raw_strip_resp[strip_num, start_idx:end_idx])
                    file_strip_averages.append((strip_num, strip_avg))
                
                all_strip_averages.extend(file_strip_averages)
                overall_averages.append(np.mean([avg for _, avg in file_strip_averages]))
            
            # Calculate the overall average across all files
            overall_avg = np.mean(overall_averages)
            
            # Store the calculation result with combined averages
            calculation_results.append(CalculationResult(
                overall_average=overall_avg,
                start_time=start_time,
                end_time=end_time,
                strip_averages=all_strip_averages
            ))
            
            # Create new calculation result
            new_calculation = create_calculation_result(calculation_results[-1])
            
            # Create new list of calculations
            if existing_content is None:
                all_calculations = [new_calculation]
            else:
                # If existing_content is a list, extend it
                if isinstance(existing_content, list):
                    all_calculations = existing_content + [new_calculation]
                # If existing_content is a Div, get its children
                else:
                    existing_calculations = existing_content.get('props', {}).get('children', [])
                    if not isinstance(existing_calculations, list):
                        existing_calculations = [existing_calculations]
                    all_calculations = existing_calculations + [new_calculation]
            
            # Update graph with new calculation result
            updated_figure = create_multi_file_figure(loaded_files, selected_strips, calculation_results)
            
            return html.Div(all_calculations), {'display': 'none'}, None, {'display': 'none'}, updated_figure
            
        except Exception as e:
            print(f"Debug - Error: {e}")
            return (
                existing_content,
                styles.BASE_POPUP,
                html.Div(f"Error processing selection: {str(e)}", style=styles.ERROR_MESSAGE),
                styles.CLOSE_BUTTON,
                dash.no_update
            )

    @app.callback(
        Output({'type': 'thickness-input', 'index': ALL}, 'value'),
        Input({'type': 'thickness-input', 'index': ALL}, 'value'),
        State({'type': 'thickness-input', 'index': ALL}, 'id')
    )
    def update_thickness(values, ids):
        """Update thickness values when they change."""
        if not values or not ids:
            return dash.no_update

        # Update thickness values in our calculation results
        for value, id_dict in zip(values, ids):
            calc_id = id_dict['index']
            # Find the calculation with matching ID
            for calc in calculation_results:
                if calc.id == calc_id:
                    # Convert to float with 2 decimal places if value is not None
                    calc.thickness = round(float(value), 2) if value is not None else None
                    break
        
        # Return float values with 2 decimal places
        return [round(float(v), 2) if v is not None else None for v in values]

    @app.callback(
        [Output('popup-message', 'style', allow_duplicate=True),
         Output('close-popup', 'style', allow_duplicate=True)],
        [Input('close-popup', 'n_clicks')],
        prevent_initial_call=True
    )
    def close_popup(n_clicks):
        if n_clicks:
            return styles.HIDDEN_POPUP, {'display': 'none'}
        return dash.no_update, dash.no_update

    @app.callback(
        Output('strip-selector', 'value'),
        [Input('select-all-button', 'n_clicks'),
         Input('unselect-all-button', 'n_clicks'),
         Input('select-odd-button', 'n_clicks'),
         Input('select-even-button', 'n_clicks')],
        [State('strip-selector', 'options')]
    )
    def update_strip_selection(select_clicks, unselect_clicks, odd_clicks, even_clicks, options):
        ctx = dash.callback_context
        if not ctx.triggered:
            return list(range(18, 153))  # Default to all selected
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        all_strips = [opt['value'] for opt in options]
        
        if button_id == 'select-all-button':
            return all_strips
        elif button_id == 'unselect-all-button':
            return []
        elif button_id == 'select-odd-button':
            return [strip for strip in all_strips if strip % 2 == 1]
        elif button_id == 'select-even-button':
            return [strip for strip in all_strips if strip % 2 == 0]
        
        return list(range(18, 153))  # Default case

    @app.callback(
        [Output('strip-selection-panel', 'style', allow_duplicate=True),
         Output('click-catcher', 'style', allow_duplicate=True),
         Output('toggle-strip-selection', 'style', allow_duplicate=True)],
        [Input('toggle-strip-selection', 'n_clicks'),
         Input('click-catcher', 'n_clicks')],
        [State('strip-selection-panel', 'style')],
        prevent_initial_call=True
    )
    def toggle_strip_selection(toggle_clicks, catcher_clicks, current_style):
        """Toggle the strip selection panel visibility."""
        ctx = dash.callback_context

        # Initial state
        if not ctx.triggered:
            return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # Handle toggle button click
        if button_id == 'toggle-strip-selection':
            # If panel is hidden (or initial state), show it
            if not current_style or current_style == styles.OVERLAY:
                return styles.OVERLAY_VISIBLE, styles.CLICK_CATCHER, dict(styles.TOGGLE_BUTTON, **{'display': 'none'})
            # If panel is visible, hide it
            return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
            
        # Handle click catcher (clicking outside panel)
        elif button_id == 'click-catcher':
            return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
        
        # Default case: no change
        return dash.no_update, dash.no_update, dash.no_update

    @app.callback(
        [Output({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
         Output({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'children')],
        Input({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'n_clicks'),
        State({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style')
    )
    def toggle_strip_averages(n_clicks, current_style):
        if n_clicks is None:
            return dash.no_update, dash.no_update
        
        is_visible = current_style.get('display', 'none') != 'none'
        
        # Update content style
        new_style = dict(current_style)
        new_style['display'] = 'none' if is_visible else 'block'
        
        # Update button icon
        new_button_children = [
            html.I(
                className="fas fa-chevron-right" if is_visible else "fas fa-chevron-down",
                style={
                    'marginRight': '8px',
                    'transition': 'transform 0.3s',
                    'transform': 'rotate(0deg)' if is_visible else 'rotate(90deg)'
                }
            ),
            html.Strong("Individual Strip Averages")
        ]
        
        return new_style, new_button_children

    @app.callback(
        [Output('strip-responses-graph', 'figure', allow_duplicate=True),
         Output('averages-content', 'children', allow_duplicate=True)],
        Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks'),
        [State('strip-selector', 'value'),
         State('averages-content', 'children')],
        prevent_initial_call=True
    )
    def delete_calculation(delete_clicks, selected_strips, existing_content):
        """Delete a calculation when the trash button is clicked."""
        if not any(click for click in delete_clicks if click):
            return dash.no_update, dash.no_update
        
        # Find which calculation was deleted
        ctx_triggered = ctx.triggered_id
        if ctx_triggered is None:
            return dash.no_update, dash.no_update
            
        deleted_id = ctx_triggered['index']
        
        # Find and remove the calculation with matching ID
        for i, calc in enumerate(calculation_results):
            if calc.id == deleted_id:
                calculation_results.pop(i)
                break
        
        # Update the calculation display
        if existing_content is None or not isinstance(existing_content, dict):
            all_calculations = []
        else:
            all_calculations = existing_content.get('props', {}).get('children', [])
            if not isinstance(all_calculations, list):
                all_calculations = [all_calculations]
        
        # Recreate all calculation displays
        updated_calculations = []
        for result in calculation_results:
            new_calc = create_calculation_result(result)
            updated_calculations.append(new_calc)
        
        # Update the graph and calculation panel
        updated_figure = create_figure(time_values, raw_strip_resp, selected_strips, calculation_results)
        return updated_figure, html.Div(updated_calculations) if updated_calculations else None

    @app.callback(
        Output('fit-graph-container', 'children', allow_duplicate=True),
        [Input({'type': 'thickness-input', 'index': ALL}, 'value'),
         Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks')],
        prevent_initial_call=True
    )
    def update_fit_graph(thickness_values, delete_clicks):
        """Update fit graph when thickness values change or calculations are deleted."""
        # Only show calculations that have thickness values
        filtered_results = [calc for calc in calculation_results if calc.thickness is not None]
        return create_fit_graph(filtered_results)

    # Function to get stored calculation results (can be used by other callbacks)
    def get_calculation_results():
        return calculation_results


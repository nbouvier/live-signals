"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL
import dash
import styles
from data_processing import create_figure
from components.calculation_result import create_calculation_result
from components.fit_graph import create_fit_graph
from models import CalculationResult

def register_callbacks(app, time_values, raw_strip_resp):
    """Register all callbacks for the application."""
    
    # Global list to store calculation results
    calculation_results = []
    
    @app.callback(
        [Output('strip-responses-graph', 'figure'),
         Output('strip-responses-graph', 'style'),
         Output('graph-placeholder', 'style'),
         Output('fit-graph-container', 'children'),
         Output('averages-content', 'children')],
        Input('url', 'pathname')
    )
    def initialize_page(pathname):
        """Reset everything when the page loads."""
        # Clear all calculations
        calculation_results.clear()
        CalculationResult.reset_id_counter()
        
        return (
            create_figure(time_values, raw_strip_resp, list(range(18, 153)), []),  # Empty figure with no selections
            styles.BASE_GRAPH,
            dict(styles.BASE_PLACEHOLDER, **{'display': 'none'}),
            create_fit_graph([]),  # Empty fit graph
            None  # Clear calculation panel
        )
    
    @app.callback(
        [Output('strip-responses-graph', 'figure', allow_duplicate=True),
         Output('strip-responses-graph', 'style', allow_duplicate=True),
         Output('graph-placeholder', 'style', allow_duplicate=True)],
        Input('strip-selector', 'value'),
        prevent_initial_call=True
    )
    def update_figure(selected_strips):
        # Handle empty strip selection
        if not selected_strips:
            return (
                create_figure(time_values, raw_strip_resp, list(range(18, 153)), []),  # Empty figure with no selections
                styles.BASE_GRAPH,
                dict(styles.BASE_PLACEHOLDER, **{'display': 'none'})
            )
        
        # Handle strip selection changes
        return (
            create_figure(time_values, raw_strip_resp, selected_strips, calculation_results),
            styles.BASE_GRAPH,  # Show graph
            dict(styles.BASE_PLACEHOLDER, **{'display': 'none'})  # Hide placeholder
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
            
            # Calculate averages
            start_idx = np.searchsorted(time_values, start_time)
            end_idx = np.searchsorted(time_values, end_time)
            
            strip_averages = []
            for strip_num in selected_strips:
                strip_avg = np.mean(raw_strip_resp[strip_num, start_idx:end_idx])
                strip_averages.append((strip_num, strip_avg))
            
            overall_avg = np.mean([avg for _, avg in strip_averages])
            
            # Store the calculation result
            calculation_results.append(CalculationResult(
                overall_average=overall_avg,
                start_time=start_time,
                end_time=end_time,
                strip_averages=strip_averages
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
            updated_figure = create_figure(time_values, raw_strip_resp, selected_strips, calculation_results)
            
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
         Input('unselect-all-button', 'n_clicks')],
        [State('strip-selector', 'options')]
    )
    def update_strip_selection(select_clicks, unselect_clicks, options):
        ctx = dash.callback_context
        if not ctx.triggered:
            return list(range(18, 153))  # Default to all selected
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'select-all-button':
            return [opt['value'] for opt in options]
        elif button_id == 'unselect-all-button':
            return []
        
        return list(range(18, 153))  # Default case

    @app.callback(
        [Output('strip-selection-panel', 'style'),
         Output('click-catcher', 'style'),
         Output('toggle-strip-selection', 'style')],
        [Input('toggle-strip-selection', 'n_clicks'),
         Input('click-catcher', 'n_clicks')],
        [State('strip-selection-panel', 'style')]
    )
    def toggle_strip_selection(toggle_clicks, catcher_clicks, current_style):
        ctx = dash.callback_context
        if not ctx.triggered:
            return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'toggle-strip-selection':
            if current_style == styles.OVERLAY:
                # Show menu
                return styles.OVERLAY_VISIBLE, styles.CLICK_CATCHER, dict(styles.TOGGLE_BUTTON, **{'display': 'none'})
            else:
                # Hide menu
                return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
        elif button_id == 'click-catcher':
            # Hide menu
            return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
        
        return current_style, {'display': 'none'}, styles.TOGGLE_BUTTON

    @app.callback(
        [Output({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
         Output({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'children')],
        Input({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'n_clicks'),
        State({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
        prevent_initial_call=True
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

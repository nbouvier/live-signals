"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL
import dash
import styles
from data_processing import create_figure, SELECTION_COLORS
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
         Output('fit-graph-container', 'children')],
        [Input('strip-selector', 'value'),
         Input({'type': 'thickness-input', 'index': ALL}, 'value')]
    )
    def update_figure(selected_strips, thickness_values):
        # Handle empty strip selection
        if not selected_strips:
            return (
                {},  # Empty figure
                dict(styles.BASE_GRAPH, **{'display': 'none'}),  # Hide graph
                styles.BASE_PLACEHOLDER,  # Show placeholder
                create_fit_graph(calculation_results)  # Add fit graph
            )
        
        # Handle strip selection changes
        return (
            create_figure(time_values, raw_strip_resp, selected_strips, calculation_results),
            styles.BASE_GRAPH,  # Show graph
            dict(styles.BASE_PLACEHOLDER, **{'display': 'none'}),  # Hide placeholder
            create_fit_graph(calculation_results)  # Add fit graph
        )

    @app.callback(
        [Output('averages-content', 'children'),
         Output('popup-message', 'style'),
         Output('popup-message-content', 'children'),
         Output('close-popup', 'style')],
        [Input('calc-button', 'n_clicks')],
        [State('strip-selector', 'value'),
         State('strip-responses-graph', 'selectedData'),
         State('averages-content', 'children')]
    )
    def update_averages(n_clicks, selected_strips, selected_data, existing_content):
        if not n_clicks:  # Skip initial callback
            return None, {'display': 'none'}, None, {'display': 'none'}

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
                    styles.CLOSE_BUTTON
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
            current_calcs = len(calculation_results)
            new_color = SELECTION_COLORS[current_calcs % len(SELECTION_COLORS)]
            calculation_results.append(CalculationResult(
                overall_average=overall_avg,
                start_time=start_time,
                end_time=end_time,
                color=new_color
            ))
            
            # Get the current number of calculations
            current_calcs = len(calculation_results)
            
            # Create new calculation result
            new_calculation = create_calculation_result(
                current_calcs,
                start_time,
                end_time,
                overall_avg,
                strip_averages,
                thickness=calculation_results[-1].thickness
            )
            
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
            
            return html.Div(all_calculations), {'display': 'none'}, None, {'display': 'none'}
            
        except Exception as e:
            print(f"Debug - Error: {e}")
            return (
                existing_content,
                styles.BASE_POPUP,
                html.Div(f"Error processing selection: {str(e)}", style=styles.ERROR_MESSAGE),
                styles.CLOSE_BUTTON
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
            index = id_dict['index']
            if index < len(calculation_results):
                # Convert to float with 2 decimal places if value is not None
                calculation_results[index].thickness = round(float(value), 2) if value is not None else None
        
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
        Output('selection-indicator', 'style'),
        [Input('strip-responses-graph', 'selectedData')]
    )
    def update_selection_indicator(selected_data):
        return dict(styles.SELECTION_INDICATOR, **{
            'backgroundColor': 'green' if selected_data else 'red'
        })

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

    # Function to get stored calculation results (can be used by other callbacks)
    def get_calculation_results():
        return calculation_results 

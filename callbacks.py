"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html
import dash
from styles import OVERLAY_STYLE, OVERLAY_VISIBLE_STYLE, TOGGLE_BUTTON_STYLE, PLACEHOLDER_STYLE
from data_processing import create_figure

def register_callbacks(app, time_values, raw_strip_resp):
    """Register all callbacks for the application."""
    
    @app.callback(
        [Output('strip-responses-graph', 'figure'),
         Output('strip-responses-graph', 'style'),
         Output('graph-placeholder', 'style')],
        [Input('strip-selector', 'value')]
    )
    def update_figure(selected_strips):
        base_graph_style = {'height': '800px', 'width': '100%'}
        base_placeholder_style = {
            'height': '800px',
            'width': '100%',
            'backgroundColor': '#f9f9f9',
            'border': '1px solid #ddd',
            'borderRadius': '5px',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'color': '#666',
            'fontSize': '18px'
        }
        
        # Handle empty strip selection
        if not selected_strips:
            return (
                {},  # Empty figure
                dict(base_graph_style, **{'display': 'none'}),  # Hide graph
                base_placeholder_style  # Show placeholder
            )
        
        # Handle strip selection changes
        return (
            create_figure(time_values, raw_strip_resp, selected_strips),
            base_graph_style,  # Show graph
            dict(base_placeholder_style, **{'display': 'none'})  # Hide placeholder
        )

    @app.callback(
        Output('averages-content', 'children'),
        [Input('calc-button', 'n_clicks')],
        [State('strip-selector', 'value'),
         State('strip-responses-graph', 'selectedData'),
         State('strip-responses-graph', 'relayoutData')]
    )
    def update_averages(n_clicks, selected_strips, selected_data, relayout_data):
        if not n_clicks:  # Skip initial callback
            return None

        try:
            # Get time range
            if selected_data and 'range' in selected_data:
                range_bounds = selected_data['range']['x']
            elif selected_data and 'points' in selected_data:
                x_values = [point['x'] for point in selected_data['points']]
                range_bounds = [min(x_values), max(x_values)]
            elif relayout_data and 'xaxis.range[0]' in relayout_data:
                range_bounds = [
                    relayout_data['xaxis.range[0]'],
                    relayout_data['xaxis.range[1]']
                ]
            elif relayout_data and 'xaxis.range' in relayout_data:
                range_bounds = relayout_data['xaxis.range']
            else:
                return html.Div("Please make a selection first", style={'color': 'red'})
                
            start_time, end_time = range_bounds
            
            # Calculate averages
            start_idx = np.searchsorted(time_values, start_time)
            end_idx = np.searchsorted(time_values, end_time)
            
            strip_averages = []
            for strip_num in selected_strips:
                strip_avg = np.mean(raw_strip_resp[strip_num, start_idx:end_idx])
                strip_averages.append((strip_num, strip_avg))
            
            overall_avg = np.mean([avg for _, avg in strip_averages])
            
            return html.Div([
                html.Div([
                    html.Strong("Time Range: "),
                    f"{start_time:.1f}ms - {end_time:.1f}ms"
                ], style={'marginBottom': '10px'}),
                html.Div([
                    html.Strong("Overall Average: "),
                    f"{overall_avg:.2f}"
                ], style={'marginBottom': '15px'}),
                html.Div([
                    html.Strong("Individual Strip Averages:", style={'display': 'block', 'marginBottom': '8px'}),
                    html.Div([
                        html.Div(f"Strip {strip_num}: {avg:.2f}", 
                                style={'marginBottom': '4px'})
                        for strip_num, avg in sorted(strip_averages)
                    ], style={'maxHeight': '300px', 'overflowY': 'auto'})
                ])
            ])
            
        except Exception as e:
            print(f"Debug - Error: {e}")
            return html.Div("Error processing selection. Please try again.", style={'color': 'red'})

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
            return OVERLAY_STYLE, {'display': 'none'}, TOGGLE_BUTTON_STYLE
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'toggle-strip-selection':
            if current_style == OVERLAY_STYLE:
                # Show menu
                return (
                    OVERLAY_VISIBLE_STYLE, 
                    {'display': 'block', 'position': 'fixed', 'top': 0, 'left': 0, 'width': '100%', 'height': '100%', 'backgroundColor': 'rgba(0,0,0,0.3)', 'zIndex': 999},
                    dict(TOGGLE_BUTTON_STYLE, **{'display': 'none'})
                )
            else:
                # Hide menu
                return OVERLAY_STYLE, {'display': 'none'}, TOGGLE_BUTTON_STYLE
        elif button_id == 'click-catcher':
            # Hide menu
            return OVERLAY_STYLE, {'display': 'none'}, TOGGLE_BUTTON_STYLE
        
        return current_style, {'display': 'none'}, TOGGLE_BUTTON_STYLE

    @app.callback(
        Output('selection-indicator', 'style'),
        [Input('strip-responses-graph', 'selectedData'),
         Input('strip-responses-graph', 'relayoutData')]
    )
    def update_selection_indicator(selected_data, relayout_data):
        base_style = {
            'width': '20px',
            'height': '20px',
            'borderRadius': '50%',
            'display': 'inline-block',
            'marginRight': '10px'
        }
        
        # Check if there's an active selection either through selectedData
        # or through the range selector in relayoutData
        selection_active = False
        
        if selected_data:
            selection_active = True
        elif relayout_data and ('xaxis.range[0]' in relayout_data or 'xaxis.range' in relayout_data):
            selection_active = True
        
        base_style['backgroundColor'] = 'green' if selection_active else 'red'
        return base_style 
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
    
    # Global list to store overall averages
    overall_averages = []
    
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
        [Output('averages-content', 'children'),
         Output('popup-message', 'style'),
         Output('popup-message-content', 'children'),
         Output('close-popup', 'style')],
        [Input('calc-button', 'n_clicks')],
        [State('strip-selector', 'value'),
         State('strip-responses-graph', 'selectedData'),
         State('strip-responses-graph', 'relayoutData'),
         State('averages-content', 'children')]
    )
    def update_averages(n_clicks, selected_strips, selected_data, relayout_data, existing_content):
        if not n_clicks:  # Skip initial callback
            return None, {'display': 'none'}, None, {'display': 'none'}

        base_popup_style = {
            'display': 'block',
            'position': 'fixed',
            'bottom': '20px',
            'right': '20px',
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '5px',
            'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
            'zIndex': 1000,
            'textAlign': 'center',
            'transition': 'transform 0.3s ease-out',
            'transform': 'translateY(0)',  # Slide up to final position
            'border': '2px solid #ff3333'
        }

        hidden_popup_style = {
            'display': 'none',
            'position': 'fixed',
            'bottom': '20px',
            'right': '20px',
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '5px',
            'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
            'zIndex': 1000,
            'textAlign': 'center',
            'transition': 'transform 0.3s ease-out',
            'transform': 'translateY(100%)',  # Start from below
            'border': '2px solid #ff3333'
        }

        base_button_style = {
            'backgroundColor': '#ff3333',
            'color': 'white',
            'border': 'none',
            'padding': '8px 16px',
            'borderRadius': '4px',
            'cursor': 'pointer',
            'display': 'block'
        }

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
                return (
                    existing_content,  # Keep existing content unchanged
                    base_popup_style,
                    html.Div("Please make a selection first", style={'color': '#ff3333', 'fontWeight': 'bold'}),
                    base_button_style
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
            
            # Store the overall average
            overall_averages.append(overall_avg)

            # Print the overall averages for debugging
            print(f"Overall averages: {overall_averages}")
            
            # Get the current number of calculations
            current_calcs = len(overall_averages)
            
            # Create new calculation result with calculation index
            new_calculation = html.Div([
                html.Hr(style={'margin': '20px 0'}),
                html.Div([
                    html.Strong("Calculation Time: "),
                    html.Span(f"Calculation #{current_calcs}", style={'color': '#666'})
                ], style={'marginBottom': '10px'}),
                html.Div([
                    html.Strong("Time Range: "),
                    f"{start_time:.1f}ms - {end_time:.1f}ms"
                ], style={'marginBottom': '10px'}),
                html.Div([
                    html.Strong("Overall Average: "),
                    html.Span(f"{overall_avg:.2f}", id={'type': 'overall-average', 'index': current_calcs - 1})
                ], style={'marginBottom': '15px'}),
                # Collapsible section for individual averages
                html.Div([
                    # Toggle button with arrow
                    html.Button([
                        html.I(className="fas fa-chevron-right", style={'marginRight': '8px', 'transition': 'transform 0.3s'}),
                        html.Strong("Individual Strip Averages")
                    ],
                    id={'type': 'toggle-strip-averages', 'index': current_calcs},
                    style={
                        'backgroundColor': 'transparent',
                        'border': 'none',
                        'padding': '8px 0',
                        'cursor': 'pointer',
                        'display': 'flex',
                        'alignItems': 'center',
                        'width': '100%',
                        'color': '#333',
                        'marginBottom': '8px'
                    }),
                    # Content (hidden by default)
                    html.Div([
                        html.Div(f"Strip {strip_num}: {avg:.2f}", 
                                style={'marginBottom': '4px'})
                        for strip_num, avg in sorted(strip_averages)
                    ],
                    id={'type': 'strip-averages-content', 'index': current_calcs},
                    style={
                        'maxHeight': '300px',
                        'overflowY': 'auto',
                        'display': 'none',
                        'padding': '10px',
                        'backgroundColor': '#fff',
                        'borderRadius': '4px',
                        'border': '1px solid #eee'
                    })
                ])
            ], style={'backgroundColor': '#f8f9fa', 'padding': '15px', 'borderRadius': '5px', 'marginBottom': '15px'})
            
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
                base_popup_style,
                html.Div(f"Error processing selection: {str(e)}", style={'color': 'red'}),
                base_button_style
            )

    @app.callback(
        [Output('popup-message', 'style', allow_duplicate=True),
         Output('close-popup', 'style', allow_duplicate=True)],
        [Input('close-popup', 'n_clicks')],
        prevent_initial_call=True
    )
    def close_popup(n_clicks):
        if n_clicks:
            hidden_style = {
                'display': 'block',  # Keep display block during animation
                'position': 'fixed',
                'bottom': '20px',
                'right': '20px',
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '5px',
                'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
                'zIndex': 1000,
                'textAlign': 'center',
                'transition': 'transform 0.3s ease-out',
                'transform': 'translateY(100%)',  # Slide down
                'border': '2px solid #ff3333'
            }
            # Use setTimeout in the frontend to actually hide the element after animation
            return hidden_style, {'display': 'none'}
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

    # Function to get stored averages (can be used by other callbacks)
    def get_stored_averages():
        return overall_averages 
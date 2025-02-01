"""
This module contains the Dash layout components for the application.
"""

from dash import html, dcc
from styles import *

def create_layout(time_values, raw_strip_resp, create_figure):
    """Create the main application layout."""
    return html.Div([
        # Click catcher
        html.Div(id='click-catcher', style={
            'position': 'fixed',
            'top': 0,
            'left': 0,
            'width': '100%',
            'height': '100%',
            'backgroundColor': 'rgba(0,0,0,0.3)',
            'zIndex': 999,
            'display': 'none'
        }),
        
        # Toggle button
        html.Button(
            '☰ Strip Selection', 
            id='toggle-strip-selection',
            style=TOGGLE_BUTTON_STYLE
        ),
        
        # Strip selection panel
        html.Div([
            html.Div([
                html.H3('Strip Selection', style={'marginBottom': '10px'}),
                html.Div([
                    html.Button(
                        'Select All', 
                        id='select-all-button', 
                        n_clicks=0,
                        style=BUTTON_STYLE
                    ),
                    html.Button(
                        'Unselect All', 
                        id='unselect-all-button', 
                        n_clicks=0,
                        style=dict(BUTTON_STYLE, **{'backgroundColor': '#f44336'})
                    ),
                ], style=BUTTON_CONTAINER_STYLE),
                dcc.Checklist(
                    id='strip-selector',
                    options=[
                        {'label': f'Strip {i}', 'value': i} 
                        for i in range(18, 153)
                    ],
                    value=list(range(18, 153)),
                    inline=True,
                    labelStyle={
                        'display': 'block',
                        'padding': '5px',
                        'backgroundColor': 'white',
                        'borderRadius': '3px',
                        'margin': '2px',
                        'cursor': 'pointer',
                        'transition': 'background-color 0.3s',
                        ':hover': {'backgroundColor': '#e6e6e6'}
                    },
                    style=STRIP_SELECTOR_STYLE
                ),
            ], style={'position': 'relative'})
        ], id='strip-selection-panel', style=OVERLAY_STYLE),
        
        # Main content
        html.Div([
            # Flex container for graph and averages
            html.Div([
                # Graph container
                html.Div([
                    # Graph
                    dcc.Loading(
                        id="loading-graph",
                        type="circle",
                        children=dcc.Graph(
                            id='strip-responses-graph',
                            figure=create_figure(time_values, raw_strip_resp),
                            style={'height': '800px', 'width': '100%'}
                        )
                    ),
                    # Placeholder (same size as graph)
                    html.Div(
                        "No data to display. Please select at least one strip.",
                        id='graph-placeholder',
                        style={
                            'display': 'none',
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
                    )
                ], style={'flex': '1 1 auto', 'minWidth': '0', 'width': '100%', 'position': 'relative'}),
                
                # Averages container
                html.Div([
                    html.H3('Calculated Averages', style={'marginTop': '0', 'marginBottom': '20px'}),
                    html.Button(
                        'Calculate Average', 
                        id='calc-button', 
                        n_clicks=0,
                        style=dict(BUTTON_STYLE, **{'backgroundColor': '#2196F3', 'width': '100%'})
                    ),
                    html.Div(id='averages-content', style={'marginTop': '20px'}),
                    # Selection indicator
                    html.Div([
                        html.Div(
                            id='selection-indicator',
                            style={
                                'width': '12px',
                                'height': '12px',
                                'backgroundColor': 'red',
                                'borderRadius': '50%',
                                'display': 'inline-block',
                                'marginRight': '8px'
                            }
                        ),
                        html.Span("Selection Active", style={'fontSize': '14px'})
                    ], style={'display': 'flex', 'alignItems': 'center', 'marginTop': '20px'})
                ], style={'flex': '0 0 300px'}),
            ], style={'display': 'flex', 'gap': '20px', 'width': '100%'}),
        ], style={'marginLeft': '60px', 'marginRight': '20px', 'width': 'calc(100% - 80px)'})]) 
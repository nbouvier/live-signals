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
        
        # Popup message
        html.Div([
            html.Div(id='popup-message-content', style={
                'color': '#ff3333',
                'fontWeight': 'bold',
                'marginBottom': '15px'
            }),
            html.Button(
                "OK",
                id='close-popup',
                style={
                    'backgroundColor': '#ff3333',
                    'color': 'white',
                    'border': 'none',
                    'padding': '8px 16px',
                    'borderRadius': '4px',
                    'cursor': 'pointer',
                    'display': 'none'
                }
            )
        ],
            id='popup-message',
            style={
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
                'transform': 'translateY(100%)',
                'border': '2px solid #ff3333'
            }
        ),
        
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
                    html.Div(id='averages-content', style={'marginBottom': '20px'}),
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
                    ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'}),
                    # Calculate button at the bottom
                    html.Button([
                        html.I(className="fas fa-plus", style={'marginRight': '8px'}),  # Plus icon
                        "Average"
                    ],
                    id='calc-button',
                    n_clicks=0,
                    style=dict(BUTTON_STYLE, **{
                        'backgroundColor': '#2196F3',
                        'width': '100%',
                        'display': 'flex',
                        'alignItems': 'center',
                        'justifyContent': 'center',
                        'gap': '8px'
                    }))
                ], style={'flex': '0 0 300px'}),
            ], style={'display': 'flex', 'gap': '20px', 'width': '100%'}),
        ], style={'marginLeft': '60px', 'marginRight': '20px', 'width': 'calc(100% - 80px)'})]) 
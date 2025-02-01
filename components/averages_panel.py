"""
This module contains the averages panel component.
"""
from dash import html
from styles import (
    BUTTON_STYLE,
    SELECTION_INDICATOR_BASE_STYLE
)

def create_averages_panel():
    """Create the averages panel component."""
    return html.Div([
        html.H3('Calculated Averages', style={'marginTop': '0', 'marginBottom': '20px'}),
        html.Div(id='averages-content', style={'marginBottom': '20px'}),
        # Selection indicator
        html.Div([
            html.Div(
                id='selection-indicator',
                style=dict(SELECTION_INDICATOR_BASE_STYLE, **{'backgroundColor': 'red'})
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
    ], style={'flex': '0 0 300px'}) 
"""
This module contains the averages panel component.
"""
from dash import html
from .averages_panel_style import *  # Import styles directly from the style file

def create_averages_panel():
    """Create the averages panel component."""
    return html.Div([
        html.H3('Calculated Averages', style=HEADER),
        html.Div(id='averages-content', style=CONTENT),
        # Selection indicator
        html.Div([
            html.Div(
                id='selection-indicator',
                style=dict(SELECTION_INDICATOR, **{'backgroundColor': 'red'})
            ),
            html.Span("Selection Active", style=INDICATOR_LABEL)
        ], style=INDICATOR_CONTAINER),
        # Calculate button at the bottom
        html.Button([
            html.I(className="fas fa-plus", style=BUTTON_ICON),  # Plus icon
            "Average"
        ],
        id='calc-button',
        n_clicks=0,
        style=CALCULATE_BUTTON)
    ], style=CONTAINER) 
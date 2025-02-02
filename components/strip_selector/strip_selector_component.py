"""
This module contains the strip selector component.
"""
from dash import html, dcc
from .strip_selector_style import *  # Import styles directly from the style file

def create_strip_selector_panel():
    """Create the strip selector panel component."""
    return html.Div([
        html.Div([
            html.H3('Strip Selection', style={'marginBottom': '10px'}),
            html.Div([
                html.Button(
                    'Select All', 
                    id='select-all-button', 
                    n_clicks=0,
                    style=BUTTON
                ),
                html.Button(
                    'Unselect All', 
                    id='unselect-all-button', 
                    n_clicks=0,
                    style=UNSELECT_BUTTON
                ),
            ], style=BUTTON_CONTAINER),
            dcc.Checklist(
                id='strip-selector',
                options=[
                    {'label': f'Strip {i}', 'value': i} 
                    for i in range(18, 153)
                ],
                value=list(range(18, 153)),
                inline=True,
                labelStyle=STRIP_LABEL,
                style=STRIP_SELECTOR
            ),
        ], style={'position': 'relative'})
    ], id='strip-selection-panel', style=OVERLAY) 
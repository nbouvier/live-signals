"""
This module contains the strip selector component.
"""
from dash import html, dcc
import styles

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
                    style=styles.BUTTON
                ),
                html.Button(
                    'Unselect All', 
                    id='unselect-all-button', 
                    n_clicks=0,
                    style=dict(styles.BUTTON, **{'backgroundColor': '#f44336'})
                ),
            ], style=styles.BUTTON_CONTAINER),
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
                style=styles.STRIP_SELECTOR
            ),
        ], style={'position': 'relative'})
    ], id='strip-selection-panel', style=styles.OVERLAY) 
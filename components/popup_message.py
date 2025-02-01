"""
This module contains the popup message component.
"""
from dash import html
import styles

def create_popup_message():
    """Create the popup message component."""
    return html.Div([
        html.Div(
            id='popup-message-content',
            style=styles.ERROR_MESSAGE
        ),
        html.Button(
            "OK",
            id='close-popup',
            style=styles.CLOSE_BUTTON
        )
    ],
    id='popup-message',
    style=dict(styles.BASE_POPUP, **{'display': 'none'})) 
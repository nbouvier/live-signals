"""
This module contains the popup message component.
"""
from dash import html
from styles import (
    BASE_POPUP_STYLE,
    CLOSE_BUTTON_STYLE,
    ERROR_MESSAGE_STYLE
)

def create_popup_message():
    """Create the popup message component."""
    return html.Div([
        html.Div(
            id='popup-message-content',
            style=ERROR_MESSAGE_STYLE
        ),
        html.Button(
            "OK",
            id='close-popup',
            style=CLOSE_BUTTON_STYLE
        )
    ],
    id='popup-message',
    style=dict(BASE_POPUP_STYLE, **{'display': 'none'})) 
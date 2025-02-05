"""
This module contains the popup message component.
"""
from dash import html
from .popup_message_callbacks import register_callbacks
from .popup_message_style import *

def create_popup_message():
    """Create the popup message component."""

    register_callbacks(app)

    return html.Div([
        html.Div(
            id='popup-message-content',

            style=ERROR_MESSAGE
        ),
        html.Button(
            "OK",
            id='close-popup',
            style=CLOSE_BUTTON
        )
    ],
    id='popup-message',
    style=dict(BASE_POPUP, **{'display': 'none'})) 

"""
This module contains the popup message component.
"""
from dash import html
from .popup_message_style import *

def popup_message():
	"""Create the popup message component."""
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

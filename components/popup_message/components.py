from dash import html
from .styles import *

def PopupMessage():
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

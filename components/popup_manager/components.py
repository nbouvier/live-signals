from dash import html, dcc
from .styles import *

def PopupList():
	return html.Div([
		html.Div([], id='popup-list', style=POPUP_LIST),

		dcc.Store(id='popups-store', data={})
	])
	
def Popup(popup):
	return html.Div([
		html.Span(popup['message'], id='popup-message-content'),
		html.I(id={'type': 'close-popup', 'popup_id': popup['id']}, className='fa-solid fa-xmark', style=POPUP_ICON)
	],
	id={'type': 'popup-message', 'popup_id': popup['id']},
	style=POPUP) 

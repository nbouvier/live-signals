from dash import Input, Output, no_update
from styles import *

def register_popup_message_callbacks(app):
	
	@app.callback(
		[Output('popup-message', 'style', allow_duplicate=True),
		 Output('close-popup', 'style', allow_duplicate=True)],
		[Input('close-popup', 'n_clicks')],
		prevent_initial_call=True
	)
	def close_popup(n_clicks):
		if n_clicks:
			return HIDDEN_POPUP, {'display': 'none'}
		return no_update, no_update



from dash import Input, Output, State, ALL, no_update, ctx
from styles import *
from .components import Popup

def register_popup_manager_callbacks(app):
	
	@app.callback(
		Output('popups-store', 'data', allow_duplicate=True),
		Input({'type': 'close-popup', 'popup_id': ALL}, 'n_clicks'),
		State('popups-store', 'data'),
		prevent_initial_call=True
	)
	def close_popup(clicks, popups):
		print('oui')
		if ctx.triggered[0]['value'] is None:
			return no_update

		popup_id = ctx.triggered_id['popup_id']
		del popups[popup_id]

		return popups
	
	@app.callback(
		Output('popup-list', 'children'),
		Input('popups-store', 'data')
	)
	def display_popup(popups):
		return [Popup(p) for p in popups.values()]



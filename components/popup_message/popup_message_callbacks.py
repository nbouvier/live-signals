"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles

def register_popup_message_callbacks(app):
	"""Register message popup callbacks."""
	
	@app.callback(
		[Output('popup-message', 'style', allow_duplicate=True),
		 Output('close-popup', 'style', allow_duplicate=True)],
		[Input('close-popup', 'n_clicks')],
		prevent_initial_call=True
	)
	def close_popup(n_clicks):
		"""Close the popup message when the close button is clicked."""
		
		if n_clicks:
			return styles.HIDDEN_POPUP, {'display': 'none'}
		return dash.no_update, dash.no_update



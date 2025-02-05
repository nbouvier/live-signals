"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from data_processing import create_figure, read_bin_file, process_file, create_multi_file_figure

def register_callbacks(app):
	"""Register message popup callbacks."""

	@app.callback(
		[Output('popup-message', 'style', allow_duplicate=True),
		 Output('close-popup', 'style', allow_duplicate=True)],
		[Input('close-popup', 'n_clicks')],
		prevent_initial_call=True
	)
	def close_popup(n_clicks):
		if n_clicks:
			return styles.HIDDEN_POPUP, {'display': 'none'}
		return dash.no_update, dash.no_update


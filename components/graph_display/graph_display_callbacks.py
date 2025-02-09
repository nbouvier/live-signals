"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import *
from .graph_display_logic import create_multi_file_figure
from .graph_display_style import *
from stores import get_store_data

def register_graph_display_callbacks(app):
	"""Register graph display callbacks."""
	
	@app.callback(
		[Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('strip-responses-graph', 'style', allow_duplicate=True),
		 Output('graph-placeholder', 'style', allow_duplicate=True)],
		[Input('add-file', 'contents'),
		 Input({'type': 'time-offset', 'index': ALL}, 'value'),
		 Input('strip-store', 'data')],
		[State('stores', 'children'),
		 State('add-file', 'filename'),
		 State({'type': 'time-offset', 'index': ALL}, 'id')],
		prevent_initial_call=True
	)

	def update_data(contents, time_offsets, strips, stores, filename, offset_ids):
		"""Handle file upload and update the graph."""

		files = get_store_data(stores, 'file-store')
		
		if not files:
			return no_update, no_update, no_update

		# Create figure with all files
		figure = create_multi_file_figure(stores, strips or [])
		
		return figure, GRAPH, HIDDEN

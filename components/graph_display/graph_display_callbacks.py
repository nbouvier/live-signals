"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import *
from .graph_display_logic import create_multi_file_figure
from .graph_display_style import *

def register_graph_display_callbacks(app):
	"""Register graph display callbacks."""
	
	@app.callback(
		[Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('strip-responses-graph', 'style', allow_duplicate=True),
		 Output('graph-placeholder', 'style', allow_duplicate=True)],
		[Input('file-store', 'data'),
		 Input('average-store', 'data'),
		 Input('strip-store', 'data')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_data(files, averages, strips, stores):
		"""Update the graph."""
		
		if not files or not strips:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		# Create figure with all files
		figure = create_multi_file_figure(stores, strips or [])
		
		return figure, GRAPH, HIDDEN

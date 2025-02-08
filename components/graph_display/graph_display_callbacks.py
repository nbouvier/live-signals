"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import *
from .graph_display_logic import create_multi_file_figure
from .graph_display_style import *
from state import AppState

def register_graph_display_callbacks(app):
	"""Register graph display callbacks."""
	
	@app.callback(
		[Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('strip-responses-graph', 'style', allow_duplicate=True),
		 Output('graph-placeholder', 'style', allow_duplicate=True)],
		[Input('add-file', 'contents'),
		 Input({'type': 'time-offset', 'index': ALL}, 'value'),
		 Input('strip-selector', 'data')],
		[State('add-file', 'filename'),
		 State({'type': 'time-offset', 'index': ALL}, 'id')],
		prevent_initial_call=True
	)
	def update_data(contents, time_offsets, selected_strips,  filename, offset_ids):
		"""Handle file upload and update the graph."""
		state = AppState.get_instance()
				
		if isinstance(ctx.triggered_id, dict) and ctx.triggered_id.get('type') == 'time-offset':
			# Update time offset for a file
			file_index = ctx.triggered_id['index']
			if file_index < len(state.loaded_files):
				try:
					state.loaded_files[file_index].time_offset = float(time_offsets[file_index]) if time_offsets[file_index] else 0
				except ValueError:
					pass

		if not state.loaded_files:
			return no_update, no_update, no_update

		# Create figure with all files
		figure = create_multi_file_figure(selected_strips or [])
		
		return figure, GRAPH, HIDDEN

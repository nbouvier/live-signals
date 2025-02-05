"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from .graph_display_logic import process_file, create_multi_file_figure
from models import CalculationResult, FileData
from state import AppState

def register_callbacks(app):
	"""Register graph display callbacks."""

	@app.callback(
		[Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('strip-responses-graph', 'style', allow_duplicate=True),
		 Output('loaded-files-list', 'children', allow_duplicate=True),
		 Output('graph-placeholder', 'style', allow_duplicate=True)],
		[Input('upload-data', 'contents'),
		 Input('add-file', 'contents'),
		 Input({'type': 'time-offset', 'index': ALL}, 'value'),
		 Input('strip-selector', 'value')],
		[State('upload-data', 'filename'),
		 State('add-file', 'filename'),
		 State({'type': 'time-offset', 'index': ALL}, 'id')],
		prevent_initial_call=True
	)
	def update_data(contents, add_contents, time_offsets, selected_strips, filename, add_filename, offset_ids):
		"""Handle file upload and update the graph."""
		ctx_triggered = ctx.triggered_id
		
		if ctx_triggered == 'upload-data' and contents:			
			try:
				# Process the file
				file_data = process_file(contents, filename)
				AppState.loaded_files.append(file_data)
			except Exception as e:
				print(f"Error processing file: {e}")
				return dash.no_update, dash.no_update, dash.no_update, dash.no_update
				

		elif isinstance(ctx_triggered, dict) and ctx_triggered.get('type') == 'time-offset':
			# Update time offset for a file
			file_index = ctx_triggered['index']
			if file_index < len(AppState.loaded_files):
				try:
					loaded_files[file_index].time_offset = float(time_offsets[file_index]) if time_offsets[file_index] else 0
				except ValueError:
					pass
					
		elif ctx_triggered == 'add-file' and add_contents:
			try:
				# Process and add new file
				file_data = process_file(add_contents, add_filename)
				AppState.loaded_files.append(file_data)
			except Exception as e:
				print(f"Error processing file: {e}")
				return dash.no_update, dash.no_update, dash.no_update, dash.no_update
		
		if not AppState.loaded_files:
			return dash.no_update, dash.no_update, dash.no_update, dash.no_update
			
		# Create file cards with time offset inputs
		file_cards = []
		for file_data in AppState.loaded_files:
			file_cards.append(html.Div([
				html.Div([
					html.Span(f"File {file_data.id}", style={'color': styles.MUTED_TEXT_COLOR, 'fontSize': '12px', 'marginBottom': '4px'}),
					html.Div([
						html.I(className="fas fa-file-binary", style={'color': styles.MUTED_TEXT_COLOR}),
						html.Span(file_data.filename)
					])
				]),
				dcc.Input(
					id={'type': 'time-offset', 'index': file_data.id},
					type='number',
					placeholder='Offset (ms)',
					value=file_data.time_offset,
					step=1,
					style=styles.TIME_OFFSET_INPUT
				)
			], style=styles.FILE_CARD))
		
		# Create figure with all files
		figure = create_multi_file_figure(selected_strips or [])
		
		return (
			figure,
			dict(styles.BASE_GRAPH, **{'display': 'block'}),
			file_cards,
			dict(styles.BASE_PLACEHOLDER, **{'display': 'none'})
		)


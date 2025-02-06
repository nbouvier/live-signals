"""
This module contains all the callback functions for the file selector component.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
from .file_selector_logic import process_file
from .file_selector_style import *
from components.graph_display import create_multi_file_figure
from state import AppState

def register_file_selector_callbacks(app):
	"""Register file selector callbacks."""
	
	@app.callback(
		[Output('file-list', 'children', allow_duplicate=True),
		 Output('no-file', 'style', allow_duplicate=True),
		 Output('add-file', 'contents'),
		 Output('add-file', 'filename'),
		 Output('add-file', 'last_modified'),],
		Input('add-file', 'contents'),
		[State('add-file', 'filename'),
		 State('file-list', 'children')],
		prevent_initial_call=True
	)
	def add_file(content, filename, files):
		state = AppState.get_instance()

		# Process and create file data
		try:
			file = process_file(content, filename)
			state.loaded_files.append(file)
		except Exception as e:
			print(f"Error processing file: {e}")
			return no_update, no_update, no_update, no_update, no_update

		# Shorten filename if too long for display
		name = filename if len(filename) <= 20 else f"{filename[0:10]}...{filename[-10:]}"

		# Display file
		files = files if files else []
		files.append(
			html.Div([
				html.Div([
					# File name
					html.Div([
						html.I(className="fa-solid fa-file"),
						html.Span(name, title=f'File {file.id} : {filename}', style=FILE_NAME)
					], style=FILE_NAME_CONTAINER),

					# Offset input
					dcc.Input(
						id={'type': 'time-offset', 'index': file.id},
						type='number',
						value=file.time_offset,
						step=1000,
						debounce=True,
						style=OFFSET_INPUT
					)
				], style=FILE_CARD_BODY),

				# Delete button
				html.Button(
					html.I(className="fas fa-trash"),
					id={'type': 'file-delete', 'index': file.id},
					className='delete-button',
					style=FILE_DELETE
				)
			], id={'type': 'file-card', 'index': file.id}, style=FILE_CARD)
		)
		
		return files, HIDDEN, None, None, None
	
	@app.callback(
		[Output('file-list', 'children', allow_duplicate=True),
		 Output('no-file', 'style', allow_duplicate=True),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True)],
		Input({'type': 'file-delete', 'index': ALL}, 'n_clicks'),
		[State('file-list', 'children'),
		 State('add-file', 'contents'),
		 State('strip-selector', 'data')],
		prevent_initial_call=True
	)
	def remove_file(n_clicks, files, data, selected_strips):
		state = AppState.get_instance()

		# Get deleted file id
		deleted_id = ctx.triggered_id['index']

		# Get the corresponding n_clicks
		n_click = [click for i, click in enumerate(n_clicks) if deleted_id == ctx.inputs_list[0][i]['id']['index']][0]

		# Do not trigger on file-card creation
		if not n_click:
			return no_update, no_update, no_update

		# Remove file from state
		for i, file in enumerate(state.loaded_files):
			if file.id == deleted_id:
				state.loaded_files.pop(i)
				break
		
		# Remove file from display
		files = [file for file in files if file['props']['id']['index'] != deleted_id]

		# Update graph with new calculation result
		graph = create_multi_file_figure(selected_strips)
		
		return files, no_update if files else NO_FILE, graph


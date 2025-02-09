"""
This module contains all the callback functions for the file selector component.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
from .file_selector_logic import process_file
from .file_selector_style import *
from components.averages_panel import update_average
from components.calculation_result import calculation_result
from components.graph_display import create_multi_file_figure
from stores import get_store_data


def register_file_selector_callbacks(app):
	"""Register file selector callbacks."""
	
	@app.callback(
		[Output('file-store', 'data', allow_duplicate=True),
		 Output('file-list', 'children', allow_duplicate=True),
		 Output('no-file', 'style', allow_duplicate=True),
		 Output('add-file', 'contents'),
		 Output('add-file', 'filename'),
		 Output('add-file', 'last_modified'),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input('add-file', 'contents'),
		[State('stores', 'children'),
		 State('add-file', 'filename'),
		 State('file-list', 'children')],
		prevent_initial_call=True
	)
	def add_file(content, stores, filename, files_html):
		# Process file
		try:
			file = process_file(content, filename)
		except Exception as e:
			print(f"Error processing file: {e}")
			return no_update, no_update, no_update, no_update, no_update, no_update, no_update

		# Add file to store
		files = get_store_data(stores, 'file-store')
		files[file['id']] = file

		# Shorten filename if too long for display
		name = filename if len(filename) <= 20 else f"{filename[0:10]}...{filename[-10:]}"

		# Display file
		files_html = files_html or []
		files_html.append(
			html.Div([
				html.Div([
					# File name
					html.Div([
						html.I(className="fa-solid fa-file"),
						html.Span(name, title=f'File {file['id']} : {filename}', style=FILE_NAME)
					], style=FILE_NAME_CONTAINER),

					# Offset input
					dcc.Input(
						id={'type': 'time-offset', 'index': file['id']},
						type='number',
						value=file['time_offset'],
						step=1000,
						debounce=True,
						style=OFFSET_INPUT
					)
				], style=FILE_CARD_BODY),

				# Delete button
				html.Button(
					html.I(className="fas fa-trash"),
					id={'type': 'file-delete', 'index': file['id']},
					className='delete-button',
					style=FILE_DELETE
				)
			], id={'type': 'file-card', 'index': file['id']}, style=FILE_CARD)
		)

		# Update calculation results
		averages = get_store_data(stores, 'average-store')
		calculation_results_html = []
		for average in averages.values():
			average = update_average(stores, average)
			calculation_results_html.append(calculation_result(average))
		
		return files, files_html, HIDDEN, None, None, None, calculation_results_html
	
	@app.callback(
		[Output('file-store', 'data', allow_duplicate=True),
		 Output('file-list', 'children', allow_duplicate=True),
		 Output('no-file', 'style', allow_duplicate=True),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input({'type': 'file-delete', 'index': ALL}, 'n_clicks'),
		[State('stores', 'children'),
		 State('file-list', 'children'),
		 State('add-file', 'contents')],
		prevent_initial_call=True
	)
	def remove_file(n_clicks, stores, files_html, data):
		# Get deleted file id
		deleted_id = ctx.triggered_id['index']

		# Get the corresponding n_clicks
		n_click = [click for i, click in enumerate(n_clicks) if deleted_id == ctx.inputs_list[0][i]['id']['index']][0]

		# Do not trigger on file-card creation
		if not n_click:
			return no_update, no_update, no_update, no_update, no_update

		# Remove file from store
		files = get_store_data(stores, 'file-store')
		del files[str(deleted_id)]
		
		# Remove file from display
		files_html = [file for file in files_html if file['props']['id']['index'] != deleted_id]

		# Update graph with new calculation result
		strips = get_store_data(stores, 'strip-store')
		graph = create_multi_file_figure(stores, strips)

		# Update calculation results
		averages = get_store_data(stores, 'average-store')
		calculation_results_html = []
		for average in averages.values():
			average = update_average(stores, average)
			calculation_results_html.append(calculation_result(average))
		
		return files, files_html, no_update if files else NO_FILE, graph, calculation_results_html
	
	@app.callback(
		[Output('file-store', 'data', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input({'type': 'time-offset', 'index': ALL}, 'value'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_offset(offsets, stores):
		# Get the corresponding file index
		file_id = ctx.triggered_id['index']

		# Get the corresponding offset
		offset = [offset for i, offset in enumerate(offsets) if file_id == ctx.inputs_list[0][i]['id']['index']][0]

		# Update file in store
		files = get_store_data(stores, 'file-store')
		files[str(file_id)]['time_offset'] = offset

		# Update calculation results
		averages = get_store_data(stores, 'average-store')
		calculation_results_html = []
		for average in averages.values():
			average = update_average(stores, average)
			calculation_results_html.append(calculation_result(average))
		
		return files, calculation_results_html


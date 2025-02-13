"""
This module contains all the callback functions for the file selector component.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
from components.averages_panel import process_average
from .file_selector_component import file
from .file_selector_logic import process_file
from .file_selector_style import *
from stores import get_store_data
from styles import *

def register_file_selector_callbacks(app):
	"""Register file selector callbacks."""

	@app.callback(
		[Output('files', 'children'),
		 Output('no-file', 'style')],
		Input('file-store', 'data')
	)
	def display_files(files):
		"""Display the files."""

		files_html = [file(f) for f in files.values()]

		return files_html, NO_FILE if not files_html else HIDDEN
	
	@app.callback(
		[Output('file-store', 'data', allow_duplicate=True),
		 Output('average-store', 'data', allow_duplicate=True),
		 Output('add-file', 'contents'),
		 Output('add-file', 'filename'),
		 Output('add-file', 'last_modified'),
		 Output('popup-message-content', 'children', allow_duplicate=True),
		 Output('popup-message', 'style', allow_duplicate=True)],
		Input('add-file', 'contents'),
		[State('stores', 'children'),
		 State('add-file', 'filename')],
		prevent_initial_call=True
	)
	def add_file(content, stores, filename):
		# Process file
		try:
			file = process_file(content, filename)
		except Exception as e:
			return (
				no_update,
				no_update,
				no_update,
				no_update,
				no_update,
				html.Div(f"Error processing file\n\n{e}", style=ERROR_MESSAGE),
				BASE_POPUP
			)

		# Add file to store
		files = get_store_data(stores, 'file-store')
		files[str(file['id'])] = file

		# Add file plateaus to averages
		averages = get_store_data(stores, 'average-store')
		for plateau in file['plateaus']:
			average = process_average(stores, plateau['time_range'], plateau['qdc_range'], file_id=file['id'])
			averages[str(average['id'])] = average
		
		return files, averages, None, None, None, None, HIDDEN
	
	@app.callback(
		Output('file-store', 'data', allow_duplicate=True),
		Input({'type': 'time-offset', 'index': ALL}, 'value'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_offset(offsets, stores):
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update

		# Get data
		file_id = ctx.triggered_id['index']
		offset = ctx.triggered[0]['value']

		# Update file in store
		files = get_store_data(stores, 'file-store')
		files[str(file_id)]['time_offset'] = offset
		
		return files
	
	@app.callback(
		[Output('file-store', 'data', allow_duplicate=True),
		 Output('average-store', 'data', allow_duplicate=True)],
		Input({'type': 'file-delete', 'index': ALL}, 'n_clicks'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def remove_file(clicks, stores):
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update, no_update

		# Get data
		file_id = ctx.triggered_id['index']

		# Remove file from store
		files = get_store_data(stores, 'file-store')
		del files[str(file_id)]

		# Remove file plateaus from averages
		averages = get_store_data(stores, 'average-store')
		averages = {a['id']: a for a in averages.values() if a['file_id'] != file_id}
		
		return files, averages


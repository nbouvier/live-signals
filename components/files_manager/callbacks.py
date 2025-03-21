from dash import Input, Output, State, ctx, html, ALL, MATCH, no_update
from .components import FilesPlaceholder, File, FileGraphs
from .logic import process_file
from .styles import *
from styles import *
from components.popup_manager import popup

def register_files_manager_callbacks(app):
	
	@app.callback(
		[Output('files', 'children', allow_duplicate=True),
		 Output('graphs', 'children', allow_duplicate=True),
		 Output('add-file', 'contents'),
		 Output('add-file', 'filename'),
		 Output('add-file', 'last_modified'),
		 Output('popups-store', 'data', allow_duplicate=True)],
		Input('add-file', 'contents'),
		[State({'type': 'file-store', 'file_id': ALL}, 'data'),
		 State('add-file', 'filename'),
		 State('file-options', 'value'),
		 State('files', 'children'),
		 State('graphs', 'children'),
		 State('popups-store', 'data')],
		prevent_initial_call=True
	)
	def add_file(content, files, filename, options, files_html, graphs_html, popups):
		try:
			file = process_file(content, filename, options=options)
		except Exception as e:
			p = popup(f"Error processing file: {e}", 'error')
			popups[p['id']] = p
			return no_update, no_update, None, None, None, popups

		files_html = [] if not files else files_html
		files_html.append(File(file))
		graphs_html.append(FileGraphs(file))
		
		return files_html, graphs_html, None, None, None, no_update

	@app.callback(
		[Output({'type': 'file-header-toggle', 'file_id': MATCH}, 'className'),
		 Output({'type': 'file-body', 'file_id': MATCH}, 'style')],
		Input({'type': 'file-header', 'file_id': MATCH}, 'n_clicks'),
	)
	def toggle_file(clicks):
		if clicks is None:
			return no_update, no_update
	
		classes = "fas fa-chevron-right" if clicks % 2 == 1 else "fas fa-chevron-down"
		style = HIDDEN if clicks % 2 == 1 else FILE_BODY
		
		return classes, style
		
	@app.callback(
		[Output('files', 'children', allow_duplicate=True),
		 Output('graphs', 'children', allow_duplicate=True)],
		Input({'type': 'delete-file', 'file_id': ALL}, 'n_clicks'),
		[State('files', 'children'),
		 State('graphs', 'children')],
		prevent_initial_call=True
	)
	def remove_file(clicks, files_html, graphs_html):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update

		file_id = ctx.triggered_id['file_id']
		files_html = [f for f in files_html if f['props']['id']['file_id'] != file_id] or FilesPlaceholder()
		graphs_html = [g for g in graphs_html if g['props']['id']['file_id'] != file_id]

		return files_html, graphs_html

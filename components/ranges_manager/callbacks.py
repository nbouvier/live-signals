from dash import Input, Output, State, ctx, ALL, MATCH, no_update
from styles import *
from .components import RangesPlaceholder, Range
from .logic import process_range, update_range, update_range_strips
from .styles import *

def register_ranges_manager_callbacks(app):
	
	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'add-range', 'file_id': MATCH}, 'n_clicks'),
		[State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		 State({'type': 'strip-responses-graph', 'file_id': MATCH}, 'selectedData')],
		prevent_initial_call=True
	)	
	def add_range(_clicks, file, selected_data):
		if not selected_data or not 'range' in selected_data:
			return no_update, no_update
		
		range = process_range(file, selected_data['range']['x'], selected_data['range']['y'])
		file['ranges'][range['id']] = range
		
		return file, list(file['ranges'].keys())

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'select-range', 'file_id': MATCH, 'range_id': ALL}, 'n_clicks'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def select_range(_clicks, file):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update

		range_id = ctx.triggered_id['range_id']
		file['ranges'][range_id]['selected'] == True
		
		for range in file['ranges'].values():
			file['ranges'][range['id']]['selected'] = range['id'] == range_id
		
		return file, list(file['ranges'].keys())
	
	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'strips-store', 'file_id': MATCH}, 'data'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)	
	def update_average(_strips, file):
		for range in file['ranges'].values():
			update_range(file, range)
			
		return file, list(file['ranges'].keys())
	
	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'selected-strips-store', 'file_id': MATCH}, 'data'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)	
	def update_average_strips(_strips, file):
		for range in file['ranges'].values():
			update_range_strips(file, range)
		
		return file, list(file['ranges'].keys())

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'thickness-input', 'file_id': MATCH, 'range_id': ALL}, 'value'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def update_thickness(values, file):
		if ctx.triggered_id is None:
			return no_update, no_update

		range_id = ctx.triggered_id['range_id']
		value = ctx.triggered[0]['value']

		if value is None and file['ranges'][range_id]['thickness'] is None:
			return no_update, no_update
			
		file['ranges'][range_id]['thickness'] = value
		
		return file, list(file['ranges'].keys())

	@app.callback(
		[Output({'type': 'strip-averages-toggle-icon', 'file_id': MATCH, 'range_id': MATCH}, 'className'),
		 Output({'type': 'strip-averages-content', 'file_id': MATCH, 'range_id': MATCH}, 'style')],
		Input({'type': 'strip-averages-toggle', 'file_id': MATCH, 'range_id': MATCH}, 'n_clicks')
	)
	def toggle_strips(clicks):
		if clicks is None:
			return no_update, no_update

		classes = "fas fa-chevron-right" if clicks % 2 == 0 else "fas fa-chevron-down"
		style = HIDDEN if clicks % 2 == 0 else STRIP_AVERAGES_CONTENT

		return classes, style

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'delete-range', 'file_id': MATCH, 'range_id': ALL}, 'n_clicks'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def delete_range(_clicks, file):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update

		range_id = ctx.triggered_id['range_id']
		del file['ranges'][range_id]

		return file, list(file['ranges'].keys())

	@app.callback(
		Output({'type': 'ranges', 'file_id': MATCH}, 'children'),
		[Input({'type': 'ranges-store', 'file_id': MATCH}, 'data'),
		 Input({'type': 'selected-strips-store', 'file_id': MATCH}, 'data')],
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def display_averages(_ranges, _strips, file):
		ranges = [Range(file, a) for a in file['ranges'].values()] or RangesPlaceholder(file)

		return ranges

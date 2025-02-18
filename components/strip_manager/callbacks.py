from dash import Input, Output, State, ALL, MATCH, ctx, no_update
from styles import *
from .components import Strip
from .logic import update_strip
from components.ranges_manager import process_range

def register_strips_manager_callbacks(app):

	@app.callback(
		[Output({'type': 'strip-list-container', 'file_id': MATCH}, 'style'),
		 Output({'type': 'toggle-strip-list-icon', 'file_id': MATCH}, 'className')],
		Input({'type': 'toggle-strip-list', 'file_id': MATCH}, 'n_clicks'),
		prevent_initial_call=True
	)
	def toggle_strip_noises(clicks):
		style = HIDDEN if clicks % 2 == 0 else None
		classes = "fas fa-chevron-right" if clicks % 2 == 0 else "fas fa-chevron-down"

		return style, classes

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'strip-noise', 'file_id': MATCH, 'strip_id': ALL}, 'value'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def update_strip_noise(_values, file):
		if ctx.triggered_id is None:
			return no_update, no_update, no_update

		strip_id = ctx.triggered_id['strip_id']
		value = ctx.triggered[0]['value']

		if value is None:
			return no_update, no_update, no_update
		
		strip = file['strips'][strip_id]
		strip['noise'] = value
		update_strip(strip)
		
		return file, list(file['strips'].keys())

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'update-strip-noise-button', 'file_id': MATCH, 'action': ALL}, 'n_clicks'),
		[State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		 State({'type': 'strip-responses-graph', 'file_id': MATCH}, 'selectedData')],
		prevent_initial_call=True
	)
	def update_strip_noise_button(_clicks, file, selected_data):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update
		
		match ctx.triggered_id['action']:
			case 'reset':
				for strip in file['strips'].values():
					strip['noise'] = 0
					update_strip(strip)

			case 'update':
				if not selected_data or not 'range' in selected_data:
					return no_update, no_update

				range = process_range(file, selected_data['range']['x'], selected_data['range']['y'])

				for strip in file['strips'].values():
					if strip['selected']:
						strip['noise'] = range['strips'][strip['id']]['average']
						update_strip(strip)

		return file, list(file['strips'].keys())

	@app.callback(
		Output({'type': 'strip-list', 'file_id': MATCH}, 'children'),
		Input({'type': 'strips-store', 'file_id': MATCH}, 'data'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def display_strips(_strips, file):
		return [Strip(file, s) for s in file['strips'].values()]

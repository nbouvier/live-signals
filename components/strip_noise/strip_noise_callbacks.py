from dash import Input, Output, State, ALL, MATCH, ctx
from styles import *
from .strip_noise_style import *
from .strip_noise_logic import update_strip
from components.averages_panel import update_range

def register_strip_noise_callbacks(app):

	@app.callback(
		[Output({'type': 'strip-list', 'file_id': MATCH}, 'style'),
		 Output({'type': 'toggle-strip-list-icon', 'file_id': MATCH}, 'className')],
		Input({'type': 'toggle-strip-list', 'file_id': MATCH}, 'n_clicks'),
		prevent_initial_call=True
	)
	def toggle_strip_noises(clicks):
		style = HIDDEN if clicks % 2 == 0 else STRIP_LIST
		classes = "fas fa-chevron-right" if clicks % 2 == 0 else "fas fa-chevron-down"

		return style, classes

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'ranges-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'strip-noise', 'file_id': MATCH, 'strip_id': ALL}, 'value'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def update_strip_noise(_values, file):
		if ctx.triggered_id is None:
			return no_update, no_update

		strip_id = ctx.triggered_id['strip_id']
		value = ctx.triggered[0]['value']

		if value is None:
			return no_update, no_update
		
		strip = file['strips'][strip_id]
		strip['noise'] = value
		file['strips'][strip_id] = update_strip(strip)

		for range in file['ranges'].values():
			update_range(file, range)
		
		return file, list(file['ranges'].keys())

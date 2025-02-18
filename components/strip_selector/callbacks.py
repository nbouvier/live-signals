from dash import Input, Output, State, ctx, ALL, MATCH, no_update
from styles import *
from .components import SelectedStrip, DropdownOption
from .styles import *

def register_strip_selector_callbacks(app):

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'select-strips-button', 'file_id': MATCH, 'strips': ALL}, 'n_clicks'),
		[State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		 State({'type': 'strip-averages-graph', 'file_id': MATCH}, 'selectedData')],
		prevent_initial_call=True
	)
	def select_strips_button(_clicks, file, selected_data):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update
		
		match ctx.triggered_id['strips']:
			case 'all':
				for strip in file['strips'].values():
					strip['selected'] = True
			case 'none':
				for strip in file['strips'].values():
					strip['selected'] = False
			case 'even':
				for strip in file['strips'].values():
					strip['selected'] = int(strip['id']) % 2 == 0
			case 'odd':
				for strip in file['strips'].values():
					strip['selected'] = int(strip['id']) % 2 == 1
			case 'filter':
				if not selected_data or not 'points' in selected_data:
					return no_update, no_update

				selected_strips = [p['x'] for p in selected_data['points']]

				for strip in file['strips'].values():
					strip['selected'] = strip['id'] in selected_strips

		return file, [s['id'] for s in file['strips'].values() if s['selected']]

	@app.callback(
		[Output({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'style', allow_duplicate=True),
		 Output({'type': 'strip-search-dropdown-icon', 'file_id': MATCH}, 'className', allow_duplicate=True),
		 Output({'type': 'strip-search-overlay', 'file_id': MATCH}, 'style', allow_duplicate=True)],
		Input({'type': 'strip-search-input', 'file_id': MATCH}, 'n_clicks'),
		prevent_initial_call=True
	)
	def open_dropdown(_clicks):
		return CUSTOM_DROPDOWN_LIST, "fas fa-chevron-down", STRIP_DROPDOWN_BACKGROUND

	@app.callback(
		Output({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'children'),
		Input({'type': 'strip-search', 'file_id': MATCH}, 'value'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def filter_dropdown_options(search, file):
		search = search or ''
		options = []

		for strip in file['strips'].values():
			if not strip['selected'] and search in strip['id']:
				options.append(DropdownOption(file, strip))

		return options

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'children', allow_duplicate=True)],
		Input({'type': 'strip-search-option', 'file_id': MATCH, 'strip_id': ALL}, 'n_clicks'),
		[State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		 State({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'children')],
		prevent_initial_call=True
	)
	def select_strip(_clicks, file, options):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update, no_update

		strip_id = ctx.triggered_id['strip_id']
		file['strips'][strip_id]['selected'] = True

		for i, option in enumerate(options):
			if option['props']['id']['strip_id'] == strip_id:
				del options[i]

		return file, [s['id'] for s in file['strips'].values() if s['selected']], options

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'selected-strip', 'file_id': MATCH, 'strip_id': ALL}, 'n_clicks'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def unselect_strip(_clicks, file):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update

		strip_id = ctx.triggered_id['strip_id']
		file['strips'][strip_id]['selected'] = False

		return file, [s['id'] for s in file['strips'].values() if s['selected']]

	@app.callback(
		[Output({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'style', allow_duplicate=True),
		 Output({'type': 'strip-search-dropdown-icon', 'file_id': MATCH}, 'className', allow_duplicate=True),
		 Output({'type': 'strip-search-overlay', 'file_id': MATCH}, 'style', allow_duplicate=True)],
		Input({'type': 'strip-search-overlay', 'file_id': MATCH}, 'n_clicks'),
		prevent_initial_call=True
	)
	def close_dropdown(_clicks):
		return HIDDEN, "fas fa-chevron-right", HIDDEN

	@app.callback(
		[Output({'type': 'selected-strips', 'file_id': MATCH}, 'children'),
		 Output({'type': 'no-selected-strip', 'file_id': MATCH}, 'style')],
		Input({'type': 'selected-strips-store', 'file_id': MATCH}, 'data'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def display_selected_strips(_strips, file):
		selected_strips = [SelectedStrip(file, s) for s in file['strips'].values() if s['selected']]

		return selected_strips, None if not selected_strips else HIDDEN

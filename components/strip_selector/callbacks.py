from dash import Input, Output, State, ctx, ALL, MATCH, no_update
from styles import *
from .components import SelectedStrip, DropdownOption
from .styles import *

def register_strip_selector_callbacks(app):

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'select-strips-button', 'file_id': MATCH, 'strips': ALL}, 'n_clicks'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def select_all_strips(_clicks, file):
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
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'strip-search', 'file_id': MATCH}, 'value'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def filter_dropdown_options(search, file):
		search = search or ''
		
		for strip in file['strips'].values():
			strip['filtered'] = strip['selected'] or search not in strip['id']
			

		return file, [s['id'] for s in file['strips'].values() if s['selected']]

	@app.callback(
		[Output({'type': 'file-store', 'file_id': MATCH}, 'data', allow_duplicate=True),
		 Output({'type': 'selected-strips-store', 'file_id': MATCH}, 'data', allow_duplicate=True)],
		Input({'type': 'strip-search-option', 'file_id': MATCH, 'strip_id': ALL}, 'n_clicks'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data'),
		prevent_initial_call=True
	)
	def select_strip(_clicks, file):
		if ctx.triggered[0]['value'] is None:
			return no_update, no_update

		strip_id = ctx.triggered_id['strip_id']
		file['strips'][strip_id]['selected'] = True

		return file, [s['id'] for s in file['strips'].values() if s['selected']]

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
		 Output({'type': 'no-selected-strip', 'file_id': MATCH}, 'style'),
		 Output({'type': 'strip-search-dropdown', 'file_id': MATCH}, 'children')],
		Input({'type': 'selected-strips-store', 'file_id': MATCH}, 'data'),
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def display_strips(_strips, file):
		selected_strips = []
		dropdown_options = []

		for strip in file['strips'].values():
			if strip['selected']:
				selected_strips.append(SelectedStrip(file, strip))
			elif not strip['filtered']:
				dropdown_options.append(DropdownOption(file, strip))

		return selected_strips, None if not selected_strips else HIDDEN, dropdown_options

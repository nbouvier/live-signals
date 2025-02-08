"""
This module contains all the callback functions for the Dash application.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import PRIMARY_COLOR, HIDDEN
from .strip_selector_style import *
from state import AppState

def register_strip_selector_callbacks(app):
	"""Register strip selector callbacks."""

	@app.callback(
		[Output('strip-dropdown-list', 'children', allow_duplicate=True),
		 Output('strip-dropdown-list', 'style', allow_duplicate=True),
		 Output('strip-dropdown-background', 'style', allow_duplicate=True)],
		[Input('strip-search-input', 'value'),
		 Input('strip-search-input-container', 'n_clicks')],
		prevent_initial_call=True
	)
	def filter_dropdown_list(search_value, n_clicks):
		"""Update the dropdown list based on search input."""

		trigger = ctx.triggered[0]['prop_id']

		# Show all strips when clicking or when there's no search value
		search = search_value if search_value else ''
		matching_strips = [i for i in range(18, 153) if search in str(i)]

		# Filter out already selected strips
		available_strips = [strip for strip in matching_strips if strip not in AppState.get_instance().selected_strips]

		dropdown_items = [
			html.Div(
				f'Strip {strip}',
				id={'type': 'select-strip', 'index': strip},
				className='strip-dropdown-item',
				style=CUSTOM_DROPDOWN_ITEM
			) for strip in available_strips
		]

		return (
			dropdown_items,
			CUSTOM_DROPDOWN_LIST if dropdown_items else HIDDEN,
			STRIP_DROPDOWN_BACKGROUND if dropdown_items else HIDDEN
		)

	@app.callback(
		[Output('strip-dropdown-list', 'children', allow_duplicate=True),
		 Output('strip-dropdown-list', 'style', allow_duplicate=True),
		 Output('strip-dropdown-background', 'style', allow_duplicate=True)],
		Input('strip-selector', 'data'),
		State('strip-dropdown-list', 'children'),
		prevent_initial_call=True
	)
	def remove_from_dropdown_list(data, options):
		"""Remove the selected strip from the dropdown list when clicked."""
		if not options:
			return no_update
		
		remaining_options = [option for option in options if option['props']['id']['index'] not in data]

		return (
			remaining_options,
			no_update if remaining_options else HIDDEN,
			no_update if remaining_options else HIDDEN
		)

	@app.callback(
		[Output('strip-dropdown-list', 'style', allow_duplicate=True),
		 Output('strip-dropdown-background', 'style', allow_duplicate=True)],
		Input('strip-dropdown-background', 'n_clicks'),
		prevent_initial_call=True
	)
	def close_dropdown_list(n_clicks):
		"""Close the dropdown list when clicking outside."""
		return HIDDEN, HIDDEN

	@app.callback(
		Output('strip-selector', 'data'),
		[Input('all-strip-button', 'n_clicks'),
		 Input('no-strip-button', 'n_clicks'),
		 Input('odd-strip-button', 'n_clicks'),
		 Input('even-strip-button', 'n_clicks'),
		 Input({'type': 'strip-tag', 'index': ALL}, 'n_clicks'),
		 Input({'type': 'select-strip', 'index': ALL}, 'n_clicks')],
		State('strip-selector', 'data'),
		prevent_initial_call=True
	)
	def update_store(select_clicks, unselect_clicks, odd_clicks, even_clicks, remove_n_clicks, select_n_clicks, current_value):
		"""Update the strip selection when the buttons are clicked."""
		state = AppState.get_instance()

		# Prevent to triggers on strip-selector creation
		if not ctx.triggered[0]['value']:
			return current_value

		trigger = ctx.triggered[0]['prop_id']
		all_strips = list(range(18, 153))

		selected_strips = current_value

		if trigger == 'all-strip-button.n_clicks':
			selected_strips = all_strips

		elif trigger == 'no-strip-button.n_clicks':
			selected_strips = []

		elif trigger == 'even-strip-button.n_clicks':
			selected_strips = [strip for strip in all_strips if strip % 2 == 0]

		elif trigger == 'odd-strip-button.n_clicks':
			selected_strips = [strip for strip in all_strips if strip % 2 == 1]

		elif '.n_clicks' in trigger:
			if 'strip-tag' in trigger:
				strip_to_remove = int(eval(trigger.split('.')[0])['index'])
				selected_strips = [strip for strip in current_value if strip != strip_to_remove]

			elif 'select-strip' in trigger:
				strip_to_add = int(eval(trigger.split('.')[0])['index'])
				selected_strips = sorted(current_value + [strip_to_add])

		# Update the state
		state.selected_strips = selected_strips

		return selected_strips

	@app.callback(
		Output('selected-strips-display', 'children'),
		Input('strip-selector', 'data')
	)
	def update_selection_display(selected_strips):
		"""Update the display of selected strips."""
		selected_strips.sort()
		return [
			html.Div(
				strip,
				id={'type': 'strip-tag', 'index': strip},
				className='delete-button',
				style=SELECTED_STRIP_TAG
			)
			for strip in selected_strips
		]

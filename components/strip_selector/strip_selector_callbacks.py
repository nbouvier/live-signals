"""
This module contains all the callback functions for the Dash application.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import PRIMARY_COLOR, HIDDEN
from components.averages_panel import update_average
from components.calculation_result import calculation_result
from .strip_selector_style import *
from stores import get_store_data

def register_strip_selector_callbacks(app):
	"""Register strip selector callbacks."""

	@app.callback(
		[Output('strip-dropdown-list', 'children', allow_duplicate=True),
		 Output('strip-dropdown-list', 'style', allow_duplicate=True),
		 Output('strip-dropdown-background', 'style', allow_duplicate=True)],
		[Input('strip-search-input', 'value'),
		 Input('strip-search-input-container', 'n_clicks')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def filter_dropdown_list(search_value, n_clicks, stores):
		"""Update the dropdown list based on search input."""

		trigger = ctx.triggered[0]['prop_id']

		# Show all strips when clicking or when there's no search value
		search = search_value if search_value else ''
		matching_strips = [i for i in range(18, 153) if search in str(i)]

		# Filter out already selected strips
		strips = get_store_data(stores, 'strip-store')
		available_strips = [strip for strip in matching_strips if strip not in strips]

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
		Input('strip-store', 'data'),
		State('strip-dropdown-list', 'children'),
		prevent_initial_call=True
	)
	def remove_from_dropdown_list(strips, options):
		"""Remove the selected strip from the dropdown list when clicked."""
		if not options:
			return no_update
		
		remaining_options = [option for option in options if option['props']['id']['index'] not in strips]

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
		Output('strip-store', 'data'),
		[Input('all-strip-button', 'n_clicks'),
		 Input('no-strip-button', 'n_clicks'),
		 Input('odd-strip-button', 'n_clicks'),
		 Input('even-strip-button', 'n_clicks'),
		 Input({'type': 'strip-tag', 'index': ALL}, 'n_clicks'),
		 Input({'type': 'select-strip', 'index': ALL}, 'n_clicks')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_store(select_clicks, unselect_clicks, odd_clicks, even_clicks, remove_n_clicks, select_n_clicks, stores):
		"""Update the strip selection when the buttons are clicked."""

		strips = get_store_data(stores, 'strip-store')

		# Prevent to triggers on strip-store creation
		if not ctx.triggered[0]['value']:
			return no_update

		trigger = ctx.triggered[0]['prop_id']
		all_strips = list(range(18, 153))

		if trigger == 'all-strip-button.n_clicks':
			strips = all_strips

		elif trigger == 'no-strip-button.n_clicks':
			strips = []

		elif trigger == 'even-strip-button.n_clicks':
			strips = [strip for strip in all_strips if strip % 2 == 0]

		elif trigger == 'odd-strip-button.n_clicks':
			strips = [strip for strip in all_strips if strip % 2 == 1]

		elif '.n_clicks' in trigger:
			if 'strip-tag' in trigger:
				strip_to_remove = int(eval(trigger.split('.')[0])['index'])
				strips = [strip for strip in strips if strip != strip_to_remove]

			elif 'select-strip' in trigger:
				strip_to_add = int(eval(trigger.split('.')[0])['index'])
				strips.append(strip_to_add)
				strips.sort()

		return strips

	@app.callback(
		[Output('selected-strips-display', 'children'),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input('strip-store', 'data'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_selection_display(strips, stores):
		"""Update the display of selected strips."""

		if strips is None:
			return no_update, no_update

		# Update strips
		strips.sort()
		strips_html = [
			html.Div(
				strip,
				id={'type': 'strip-tag', 'index': strip},
				className='delete-button',
				style=SELECTED_STRIP_TAG
			)
			for strip in strips
		]

		# Update calculation results
		averages = get_store_data(stores, 'average-store')
		calculation_results_html = []
		for average in averages.values():
			average = update_average(stores, average)
			calculation_results_html.append(calculation_result(average))

		return strips_html, calculation_results_html

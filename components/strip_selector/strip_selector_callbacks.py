"""
This module contains all the callback functions for the Dash application.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import *
from .strip_selector_component import strip, strip_option
from .strip_selector_style import *
from stores import get_store_data

def register_strip_selector_callbacks(app):
	"""Register strip selector callbacks."""

	@app.callback(
		[Output('strips', 'children'),
		 Output('no-strip', 'style')],
		Input('strip-store', 'data')
	)
	def display_strips(strips):
		"""Display the strips."""

		strips_html = [strip(s) for s in strips]

		return strips_html, NO_STRIP if not strips_html else HIDDEN


	@app.callback(
		[Output('strip-dropdown-list', 'children', allow_duplicate=True),
		 Output('strip-dropdown-list', 'style', allow_duplicate=True),
		 Output('strip-dropdown-background', 'style', allow_duplicate=True)],
		[Input('strip-search-input', 'value'),
		 Input('strip-search-input-container', 'n_clicks')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def filter_dropdown_list(search_value, clicks, stores):
		"""Update the dropdown list based on search input."""

		trigger = ctx.triggered[0]['prop_id']

		# Show all strips when clicking or when there's no search value
		search = search_value if search_value else ''
		matching_strips = [i for i in range(18, 153) if search in str(i)]

		# Filter out already selected strips
		strips = get_store_data(stores, 'strip-store')

		# Update display
		available_strips = [strip_option(strip) for strip in matching_strips if strip not in strips]

		return (
			available_strips,
			CUSTOM_DROPDOWN_LIST if available_strips else HIDDEN,
			STRIP_DROPDOWN_BACKGROUND if available_strips else HIDDEN
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
	def close_dropdown_list(clicks):
		"""Close the dropdown list when clicking outside."""
		return HIDDEN, HIDDEN

	@app.callback(
		Output('strip-store', 'data'),
		[Input('all-strip-button', 'n_clicks'),
		 Input('no-strip-button', 'n_clicks'),
		 Input('odd-strip-button', 'n_clicks'),
		 Input('even-strip-button', 'n_clicks'),
		 Input({'type': 'select-strip', 'index': ALL}, 'n_clicks'),
		 Input({'type': 'strip-tag', 'index': ALL}, 'n_clicks')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_store(all_clicks, none_clicks, odd_clicks, even_clicks, add_clicks, remove_clicks, stores):
		"""Update the strip selection when the buttons are clicked."""
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update

		strips = get_store_data(stores, 'strip-store')

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

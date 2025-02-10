"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from styles import *
from .averages_panel_component import average
from .averages_panel_logic import process_average, update_average
from .averages_panel_style import *
from stores import get_store_data

def register_averages_panel_callbacks(app):
	"""Register averages panel callbacks."""

	@app.callback(
		[Output('averages', 'children'),
		 Output('no-average', 'style')],
		Input('average-store', 'data')
	)
	def display_averages(averages):
		"""Display the averages."""

		averages_html = [average(a) for a in averages.values()]

		return averages_html, NO_AVERAGE if not averages_html else HIDDEN

	@app.callback(
		Output('average-store', 'data', allow_duplicate=True),
		[Input('file-store', 'data'),
		 Input('strip-store', 'data')],
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_averages(files, strips, stores):
		"""Update the averages."""
		averages = get_store_data(stores, 'average-store')
		return {a['id']: update_average(stores, a) for a in averages.values()}
	
	@app.callback(
		[Output('average-store', 'data', allow_duplicate=True),
		 Output('popup-message-content', 'children', allow_duplicate=True),
		 Output('popup-message', 'style', allow_duplicate=True)],
		Input('add-average', 'n_clicks'),
		[State('stores', 'children'),
		 State('strip-responses-graph', 'selectedData')],
		prevent_initial_call=True
	)
	def add_average(clicks, stores, selected_data):
		"""Add an average when the add button is clicked."""

		# Handle no data selected
		if not selected_data or not 'range' in selected_data:
			return (
				no_update,
				html.Div("Please make a selection first", style=ERROR_MESSAGE),
				BASE_POPUP
			)

		# Get time range
		start_time, end_time = selected_data['range']['x']
		
		# Create a new average
		average = process_average(stores, start_time, end_time)

		# Add average to store
		averages = get_store_data(stores, 'average-store')
		averages[average['id']] = average
		
		return averages, None, HIDDEN

	@app.callback(
		Output('average-store', 'data', allow_duplicate=True),
		Input({'type': 'thickness-input', 'index': ALL}, 'value'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_thickness(values, stores):
		"""Update thickness value when it changes."""
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update
		
		# Get data
		average_id = ctx.triggered_id['index']
		value = ctx.triggered[0]['value']

		# Update average in store
		averages = get_store_data(stores, 'average-store')
		averages[str(average_id)]['thickness'] = value

		return averages

	@app.callback(
		[Output({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
		 Output({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'children')],
		Input({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'n_clicks'),
		State({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style')
	)
	def toggle_strip_averages(clicks, current_style):
		"""Toggle strip averages content when the button is clicked."""
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update, no_update

		# Fetch visibility
		is_visible = current_style.get('display', 'none') != 'none'
		
		# Update content style
		new_style = dict(current_style)
		new_style['display'] = 'none' if is_visible else 'block'
		
		# Update button icon
		new_button_children = [
			html.I(
				className="fas fa-chevron-right" if is_visible else "fas fa-chevron-down",
				style={
					'marginRight': '8px',
					'transition': 'transform 0.3s',
					'transform': 'rotate(0deg)' if is_visible else 'rotate(90deg)'
				}
			),
			html.Strong("Individual Strip Averages")
		]
		
		return new_style, new_button_children

	@app.callback(
		Output('average-store', 'data', allow_duplicate=True),
		Input({'type': 'delete-average', 'index': ALL}, 'n_clicks'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def delete_average(clicks, stores):
		"""Delete an average."""
		# Prevent trigger when no input
		if not ctx.triggered or ctx.triggered[0]['value'] is None:
			return no_update

		# Get data
		average_id = ctx.triggered_id['index']

		# Delete average from store
		averages = get_store_data(stores, 'average-store')
		del averages[str(average_id)]

		return averages

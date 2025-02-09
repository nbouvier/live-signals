"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
import styles
from components.graph_display import create_multi_file_figure
from .averages_panel_component import average as average_component
from .averages_panel_logic import process_average
from stores import get_store_data

def register_averages_panel_callbacks(app):
	"""Register averages panel callbacks."""
	
	@app.callback(
		[Output('average-store', 'data', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True),
		 Output('popup-message', 'style'),
		 Output('popup-message-content', 'children'),
		 Output('close-popup', 'style'),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True)],
		Input('calc-button', 'n_clicks'),
		[State('stores', 'children'),
		 State('strip-responses-graph', 'selectedData'),
		 State('averages-content', 'children')],
		prevent_initial_call=True
	)
	def add_average(n_clicks, stores, selected_data, averages_html):
		"""Add an average when the add button is clicked."""

		# Handle no data selected
		if not 'range' in selected_data:
			return (
				no_update,
				no_update,
				styles.BASE_POPUP,
				html.Div("Please make a selection first", style=styles.ERROR_MESSAGE),
				no_update,
				no_update
			)

		# Get time range
		start_time, end_time = selected_data['range']['x']
		
		# Create a new average
		average = process_average(stores, start_time, end_time)

		# Add average to store
		averages = get_store_data(stores, 'average-store')
		averages[average['id']] = average
		
		# Create new average element
		average_html = average_component(average)

		# Update display
		averages_html = averages_html or []
		averages_html.append(average_html)
		
		# Update graph with new average
		strips = get_store_data(stores, 'strip-store')
		updated_figure = create_multi_file_figure(stores, strips)
		
		return averages, averages_html, {'display': 'none'}, None, {'display': 'none'}, updated_figure

	@app.callback(
		Output('average-store', 'data', allow_duplicate=True),
		Input({'type': 'thickness-input', 'index': ALL}, 'value'),
		State('stores', 'children'),
		prevent_initial_call=True
	)
	def update_thickness(values, stores):
		"""Update thickness value when it changes."""

		if not values:
			return no_update

		# Get updated thickness id
		updated_id = ctx.triggered_id['index']

		# Get the corresponding value
		value = [value for i, value in enumerate(values) if updated_id == ctx.inputs_list[0][i]['id']['index']][0]

		# Update average in store
		averages = get_store_data(stores, 'average-store')
		averages[str(updated_id)]['thickness'] = value

		return averages

	@app.callback(
		[Output({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
		 Output({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'children')],
		Input({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'n_clicks'),
		State({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style')
	)
	def toggle_strip_averages(n_clicks, current_style):
		"""Toggle strip averages content when the button is clicked."""

		if n_clicks is None:
			return no_update, no_update
		
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
		[Output('average-store', 'data', allow_duplicate=True),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input({'type': 'delete-average', 'index': ALL}, 'n_clicks'),
		[State('stores', 'children'),
		 State('averages-content', 'children')],
		prevent_initial_call=True

	)
	def delete_average(delete_clicks, stores, averages_html):
		"""Delete an average."""
		
		if not any(click for click in delete_clicks if click):
			return no_update, no_update, no_update
			
		deleted_id = ctx.triggered_id['index']

		# Delete average from store
		averages = get_store_data(stores, 'average-store')
		del averages[str(deleted_id)]
		
		# Update the average display
		averages_html = [average for average in averages_html if average['props']['id']['index'] != deleted_id]
		
		# Update graph with new average
		strips = get_store_data(stores, 'strip-store')
		updated_figure = create_multi_file_figure(stores, strips)

		return averages, updated_figure, averages_html

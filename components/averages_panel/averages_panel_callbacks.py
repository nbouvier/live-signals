"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
import styles
from components.graph_display import create_multi_file_figure
from components.calculation_result import calculation_result as calculation_result_component
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
	def add_average(n_clicks, stores, selected_data, calculation_results_html):
		"""Add an average when the calculation button is clicked."""

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
		
		# Create a new calculation result
		calculation_result = process_average(stores, start_time, end_time)

		# Add average to store
		averages = get_store_data(stores, 'average-store')
		averages[calculation_result['id']] = calculation_result
		
		# Create new calculation result element
		calculation_result_html = calculation_result_component(calculation_result)

		# Create new list of calculations
		calculation_results_html = calculation_results_html or []
		calculation_results_html.append(calculation_result_html)
		
		# Update graph with new calculation result
		strips = get_store_data(stores, 'strip-store')
		updated_figure = create_multi_file_figure(stores, strips)
		
		return averages, calculation_results_html, {'display': 'none'}, None, {'display': 'none'}, updated_figure

	@app.callback(
		[Output('average-store', 'data', allow_duplicate=True),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks'),
		[State('stores', 'children'),
		 State('averages-content', 'children')],
		prevent_initial_call=True

	)
	def delete_calculation(delete_clicks, stores, calculation_results_html):
		"""Delete a calculation when the trash button is clicked."""
		
		if not any(click for click in delete_clicks if click):
			return no_update, no_update, no_update
			
		deleted_id = ctx.triggered_id['index']

		# Delete average from store
		averages = get_store_data(stores, 'average-store')
		del averages[str(deleted_id)]
		
		# Update the calculation display
		calculation_results_html = [calculation_result for calculation_result in calculation_results_html if calculation_result['props']['id']['index'] != deleted_id]
		
		# Update graph with new calculation result
		strips = get_store_data(stores, 'strip-store')
		updated_figure = create_multi_file_figure(stores, strips)

		return averages, updated_figure, calculation_results_html

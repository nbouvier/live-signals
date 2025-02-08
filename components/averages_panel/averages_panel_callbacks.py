"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
import styles
from components.graph_display import create_multi_file_figure
from components.calculation_result import calculation_result
from models import CalculationResult, FileData
from state import AppState

def register_averages_panel_callbacks(app):
	"""Register averages panel callbacks."""
	
	@app.callback(
		[Output('averages-content', 'children', allow_duplicate=True),
		 Output('popup-message', 'style'),
		 Output('popup-message-content', 'children'),
		 Output('close-popup', 'style'),
		 Output('strip-responses-graph', 'figure', allow_duplicate=True)],
		Input('calc-button', 'n_clicks'),
		[State('strip-selector', 'data'),
		 State('strip-responses-graph', 'selectedData'),
		 State('averages-content', 'children')],
		prevent_initial_call=True
	)
	def add_average(n_clicks, selected_strips, selected_data, existing_content):
		"""Add an average when the calculation button is clicked."""
		state = AppState.get_instance()

		# Handle no data selected
		if not 'range' in selected_data:
			return (
				no_update,
				styles.BASE_POPUP,
				html.Div("Please make a selection first", style=styles.ERROR_MESSAGE),
				no_update,
				no_update
			)

		# Get time range
		start_time, end_time = selected_data['range']['x']

		# Calculate averages for each file
		all_strip_averages, overall_averages = [], []
		for file_data in state.loaded_files:
			# Adjust time range for this file's offset
			adjusted_start = start_time - file_data.time_offset
			adjusted_end = end_time - file_data.time_offset
			
			# Find indices in the adjusted time range
			start_idx = np.searchsorted(file_data.time_values, adjusted_start)
			end_idx = np.searchsorted(file_data.time_values, adjusted_end)

			# Stop if signal is not in range
			if start_idx == end_idx:
				continue

			# Calculate strip averages for this file
			file_strip_averages = []
			for strip_num in selected_strips:
				strip_avg = np.mean(file_data.raw_strip_resp[strip_num, start_idx:end_idx])
				file_strip_averages.append((strip_num, strip_avg))
			
			all_strip_averages.extend(file_strip_averages)
			overall_averages.append(np.mean([avg for _, avg in file_strip_averages]))
		
		# Calculate the overall average across all files
		overall_avg = np.mean(overall_averages)
		
		# Store the calculation result with combined averages
		state.calculation_results.append(CalculationResult(
			overall_average=overall_avg,
			start_time=start_time,
			end_time=end_time,
			strip_averages=all_strip_averages
		))
		
		# Create new calculation result
		new_calculation = calculation_result(app, state.calculation_results[-1])
		
		# Create new list of calculations
		if existing_content is None:
			all_calculations = [new_calculation]
		else:
			# If existing_content is a list, extend it
			if isinstance(existing_content, list):
				all_calculations = existing_content + [new_calculation]
			# If existing_content is a Div, get its children
			else:
				existing_calculations = existing_content.get('props', {}).get('children', [])
				if not isinstance(existing_calculations, list):
					existing_calculations = [existing_calculations]
				all_calculations = existing_calculations + [new_calculation]
		
		# Update graph with new calculation result
		updated_figure = create_multi_file_figure(selected_strips)
		
		return all_calculations, {'display': 'none'}, None, {'display': 'none'}, updated_figure

	@app.callback(
		[Output('strip-responses-graph', 'figure', allow_duplicate=True),
		 Output('averages-content', 'children', allow_duplicate=True)],
		Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks'),
		[State('strip-selector', 'data'),
		 State('averages-content', 'children')],
		prevent_initial_call=True
	)
	def delete_calculation(delete_clicks, selected_strips, existing_content):
		"""Delete a calculation when the trash button is clicked."""

		state = AppState.get_instance()
		
		if not any(click for click in delete_clicks if click):
			return dash.no_update, dash.no_update
			
		deleted_id = ctx.triggered_id['index']
		
		# Find and remove the calculation with matching ID
		for i, calc in enumerate(state.calculation_results):
			if calc.id == deleted_id:
				state.calculation_results.pop(i)
				break

		# Update the calculation display
		if existing_content is None or not isinstance(existing_content, dict):
			all_calculations = []
		else:
			all_calculations = existing_content.get('props', {}).get('children', [])
			if not isinstance(all_calculations, list):
				all_calculations = [all_calculations]
		
		# Recreate all calculation displays
		updated_calculations = []
		for result in state.calculation_results:
			updated_calculations.append(calculation_result(app, result))
		
		# Update graph with new calculation result
		updated_figure = create_multi_file_figure(selected_strips)
		return updated_figure, html.Div(updated_calculations) if updated_calculations else None

"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from models import CalculationResult, FileData
from state import AppState

def register_calculation_result_callbacks(app):
	"""Register calculation result callbacks."""
	
	@app.callback(
		Output({'type': 'thickness-input', 'index': ALL}, 'value'),
		Input({'type': 'thickness-input', 'index': ALL}, 'value'),
		State({'type': 'thickness-input', 'index': ALL}, 'id')
	)
	def update_thickness(values, ids):
		"""Update thickness values when they change."""

		if not values or not ids:
			return dash.no_update

		# Update thickness values in our calculation results
		for value, id_dict in zip(values, ids):
			calc_id = id_dict['index']
			# Find the calculation with matching ID
			for calc in AppState.calculation_results:
				if calc.id == calc_id:
					# Convert to float with 2 decimal places if value is not None
					calc.thickness = round(float(value), 2) if value is not None else None
					break
		
		# Return float values with 2 decimal places
		return [round(float(v), 2) if v is not None else None for v in values]

	@app.callback(
		[Output({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style'),
		 Output({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'children')],
		Input({'type': 'toggle-strip-averages', 'index': dash.MATCH}, 'n_clicks'),
		State({'type': 'strip-averages-content', 'index': dash.MATCH}, 'style')
	)
	def toggle_strip_averages(n_clicks, current_style):
		"""Toggle strip averages content when the button is clicked."""

		if n_clicks is None:
			return dash.no_update, dash.no_update
		
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

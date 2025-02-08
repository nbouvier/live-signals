"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
import styles
from state import AppState

def register_calculation_result_callbacks(app):
	"""Register calculation result callbacks."""
	
	@app.callback(
		[],
		Input({'type': 'thickness-input', 'index': ALL}, 'value')
	)
	def update_thickness(values):
		"""Update thickness values when they change."""
		state = AppState.get_instance()

		# Get updated thickness id
		updated_id = ctx.triggered_id['index']

		# Get the corresponding value
		value = [value for i, value in enumerate(values) if updated_id == ctx.inputs_list[0][i]['id']['index']][0]

		# Update calculation result's thickness
		for calc in state.calculation_results:
			if calc.id == updated_id:
				calc.thickness = value
				break

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

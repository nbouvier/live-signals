"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
from .fit_graph_logic import create_fit_graph, calc_mu, exponential_model
from .fit_graph_style import *
from models import CalculationResult, FileData
from state import AppState

def register_fit_graph_callbacks(app):
	"""Register fit graph callbacks."""
	
	@app.callback(
		[Output('fit-graph', 'figure', allow_duplicate=True),
		 Output('fit-graph-placeholder', 'children')],
		[Input({'type': 'thickness-input', 'index': ALL}, 'value'),
		 Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks')],
		prevent_initial_call=True
	)
	def update_fit_graph(thickness_values, delete_clicks):
		"""Update fit graph when thickness values change or calculations are deleted."""

		state = AppState.get_instance()
		
		# Only show calculations that have thickness values
		filtered_results = [calc for calc in state.calculation_results if calc.thickness is not None]

		# Extract valid thickness-average pairs
		valid_pairs = [(r.thickness, r.overall_average) 
						for r in filtered_results 
						if r.thickness is not None]

		if len(valid_pairs) < 2:
			return (
				None,
				html.Div("No data points available for fitting", style=NO_DATA_MESSAGE)
			)

		# Extract thicknesses and averages
		thicknesses, averages = zip(*valid_pairs)
		thicknesses = np.array(thicknesses)
		averages = np.array(averages)
		
		# Calculate fit
		a, b = calc_mu(thicknesses, averages)
		if a is None or b is None:
			return (
				None,
				html.Div("Unable to calculate exponential fit", style=NO_DATA_MESSAGE)
			)

		# Generate points for the fit line
		x_fit = np.linspace(0, max(thicknesses), 100)
		y_fit = exponential_model(x_fit, a, b)

		return (
			create_fit_graph(thicknesses, averages, x_fit, y_fit),
			None
		)

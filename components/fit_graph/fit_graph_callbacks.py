"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
import dash
from .fit_graph_logic import create_fit_graph, calc_mu, exponential_model
from .fit_graph_style import *

def register_fit_graph_callbacks(app):
	"""Register fit graph callbacks."""
	
	@app.callback(
		[Output('fit-graph', 'figure'),
		 Output('fit-graph', 'style'),
		 Output('fit-graph-placeholder', 'style')],
		Input('average-store', 'data'),
		prevent_initial_call=True
	)
	def update_fit_graph(averages):
		"""Update fit graph."""

		filtered_averages = [average for average in averages.values() if average['average'] is not None]

		if len(filtered_averages) < 2:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		# Extract thicknesses and averages
		thicknesses = [average['thickness'] for average in filtered_averages]
		averages = [average['average'] for average in filtered_averages]

		# Calculate fit
		a, b = calc_mu(thicknesses, averages)

		if a is None or b is None:
			return no_update, no_update, no_update

		# Generate points for the fit line
		x_fit = np.linspace(0, max(thicknesses), 100)
		y_fit = exponential_model(x_fit, a, b)

		# Create graph
		figure = create_fit_graph(thicknesses, averages, x_fit, y_fit, b)

		return figure, GRAPH, HIDDEN

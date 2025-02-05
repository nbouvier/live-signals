"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from components.fit_graph import create_fit_graph
from models import CalculationResult, FileData
from state import AppState

def register_callbacks(app):
	"""Register fit graph callbacks."""

	@app.callback(
		Output('fit-graph-container', 'children', allow_duplicate=True),
		[Input({'type': 'thickness-input', 'index': ALL}, 'value'),
		 Input({'type': 'delete-calculation', 'index': ALL}, 'n_clicks')],
		prevent_initial_call=True
	)
	def update_fit_graph(thickness_values, delete_clicks):
		"""Update fit graph when thickness values change or calculations are deleted."""
		# Only show calculations that have thickness values
		filtered_results = [calc for calc in AppState.calculation_results if calc.thickness is not None]
		return create_fit_graph(app, filtered_results)

"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from models import CalculationResult, FileData
from state import AppState
from components.graph_display import register_graph_display_callbacks
from components.strip_selector import register_strip_selector_callbacks 
from components.averages_panel import register_averages_panel_callbacks
from components.fit_graph import register_fit_graph_callbacks

def register_callbacks(app):
	"""Register all callbacks for the application."""

	register_strip_selector_callbacks(app)
	register_graph_display_callbacks(app)
	register_averages_panel_callbacks(app)
	register_fit_graph_callbacks(app)

	@app.callback([], Input('url', 'pathname'))
	def initialize_page(pathname):
		"""Reset everything when the page loads."""
		AppState.get_instance().reset()

"""
This module contains the layout of the application.
"""

from dash import html, dcc
from styles import *
from components.averages_panel import averages_panel
from components.file_selector import file_selector
from components.fit_graph import fit_graph
from components.graph_display import graph_display
from components.strip_selector import strip_selector
from callbacks import register_callbacks

def create_layout(app):
	"""Create the application layout."""

	register_callbacks(app)

	return html.Div([
		# URL Location component for page initialization
		dcc.Location(id='url', refresh=False),

		# Left panel - Strip selector
		html.Div([
			file_selector(app),
			strip_selector(app),
			averages_panel(app)
		], style=SIDE_PANEL),

		# Center panel - Graph display
		html.Div([
			graph_display(app),
			fit_graph(app)
		], style=CENTER_PANEL),
		
		# Popup message
		html.Div([
			html.Div(id='popup-message-content'),
			html.Button(
				html.I(className="fas fa-times"),
				id='close-popup',
				style=CLOSE_BUTTON
			)
		], id='popup-message', style=HIDDEN_POPUP)
	], style=MAIN_CONTAINER)

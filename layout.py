"""
This module contains the layout of the application.
"""

from dash import html, dcc
from styles import *
from components.averages_panel import average_store, averages_panel, register_averages_panel_callbacks
from components.file_selector import file_store, file_selector, register_file_selector_callbacks
from components.fit_graph import fit_graph, register_fit_graph_callbacks
from components.graph_display import graph_display, register_graph_display_callbacks
from components.popup_message import register_popup_message_callbacks
from components.strip_graph import strip_graph, register_strip_graph_callbacks
from components.strip_selector import strip_store, strip_selector, register_strip_selector_callbacks

def create_layout(app):
	"""Create the application layout."""

	register_averages_panel_callbacks(app)
	register_file_selector_callbacks(app)
	register_fit_graph_callbacks(app)
	register_graph_display_callbacks(app)
	register_popup_message_callbacks(app)
	register_strip_graph_callbacks(app)
	register_strip_selector_callbacks(app)

	return html.Div([
		# URL Location component for page initialization
		dcc.Location(id='url', refresh=False),

		# Left panel - Strip selector
		html.Div([
			file_selector(),
			strip_selector(),
			averages_panel()
		], style=SIDE_PANEL),

		# Center panel - Graph display
		html.Div([
			graph_display(),
			html.Div([
				strip_graph(),
				fit_graph()
			], style={'display': 'flex', 'gap': '16px'})
		], style=CENTER_PANEL),
		
		# Popup message
		html.Div([
			html.Div(id='popup-message-content'),
			html.Button(
				html.I(className="fas fa-times"),
				id='close-popup',
				style=CLOSE_BUTTON
			)
		], id='popup-message', style=HIDDEN_POPUP),

		html.Div([
			file_store(),
			strip_store(),
			average_store()
		], id='stores', style=HIDDEN)
	], style=MAIN_CONTAINER)

"""
This module contains the layout of the application.
"""

from dash import html, dcc
from styles import *
from callbacks import register_callbacks
from components.averages_panel import register_averages_panel_callbacks
from components.file_selector import FileSelector, register_file_selector_callbacks
from components.fit_graph import exponential_fit_graph, register_exponential_fit_graph_callbacks
from components.graph_display import register_strip_responses_graph_callbacks
from components.popup_message import register_popup_message_callbacks
from components.strip_graph import register_strip_averages_graph_callbacks
from components.strip_selector import register_strip_selector_callbacks

def create_layout(app):
	"""Create the application layout."""

	register_callbacks(app)
	register_averages_panel_callbacks(app)
	register_exponential_fit_graph_callbacks(app)
	register_file_selector_callbacks(app)
	register_popup_message_callbacks(app)
	register_strip_averages_graph_callbacks(app)
	register_strip_responses_graph_callbacks(app)
	register_strip_selector_callbacks(app)

	return html.Div([
		# URL Location component for page initialization
		dcc.Location(id='url', refresh=False),

		# Left panel
		html.Div(FileSelector(), id='side-panel', style=SIDE_PANEL),
		html.Div([
			html.Div([
				html.I(id={'type': 'toggle-side-panel-icon', 'id': 1}, className="fas fa-chevron-left"),
				html.I(id={'type': 'toggle-side-panel-icon', 'id': 2}, className="fas fa-chevron-left")
			], id='toggle-side-panel', style=TOGGLE_SIDE_PANEL)
		], id='toggle-side-panel-container', style=TOGGLE_SIDE_PANEL_CONTAINER),

		# Center panel
		html.Div([
			html.Div([], id='graphs', className='flex medium-gap', style=GRAPHS_CONTAINER),
			exponential_fit_graph()
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
	], style=MAIN_CONTAINER)

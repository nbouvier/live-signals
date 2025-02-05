"""
This module contains the averages panel component.
"""
from dash import html
from .averages_panel_callbacks import register_callbacks
from .averages_panel_style import *

def averages_panel(app):
	"""Create the averages panel component."""

	register_callbacks(app)

	return html.Div([
		html.Button([
			html.I(className="fas fa-plus", style=BUTTON_ICON),
			"Average"
		], id='calc-button', style=CALCULATE_BUTTON),
		html.Div(id='averages-content', style=AVERAGES_CONTENT)
	], style=CONTAINER) 

"""
This module contains the averages panel component.
"""
from dash import html, dcc
from .averages_panel_style import *

def averages_panel():
	"""Create the averages panel component."""
	return html.Div([
		html.Button([
			html.I(className="fas fa-plus", style=BUTTON_ICON),
			"Average"
		], id='calc-button', style=CALCULATE_BUTTON),
		
		html.Div(id='averages-content', style=AVERAGES_CONTENT)
	])

def average_store():
	"""Create the average store component."""
	return dcc.Store(id='average-store', data={})

"""
This module contains the averages panel component.
"""
from dash import html
from .averages_panel_style import *  # Import styles directly from the style file

def create_averages_panel():
    """Create the averages panel component."""
    return html.Div([
		html.Button([
			html.I(className="fas fa-plus", style=BUTTON_ICON),  # Plus icon
			"Average"
		], id='calc-button', style=CALCULATE_BUTTON),
        html.Div(id='averages-content', style=AVERAGES_CONTENT)
    ], style=CONTAINER) 

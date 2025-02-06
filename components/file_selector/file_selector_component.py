"""
This module contains the graph display component.
"""
from dash import html, dcc
from .file_selector_style import *

def file_selector(app):
	"""Create the file selector component."""
	return html.Div([
		# Add file button
		dcc.Upload(
			id='add-file',
			children=html.Button([
				html.I(className="fas fa-plus", style=BUTTON_ICON),
				"File"
			], style=ADD_FILE_BUTTON)
		),

		# Loaded files list
		html.Div(id='file-list', style=FILES_LIST),
		html.Div("No file loaded.", id='no-file', style=NO_FILE)
	])

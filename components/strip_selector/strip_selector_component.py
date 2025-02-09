"""
This module contains the strip selector component.
"""
from dash import html, dcc
from .strip_selector_style import *

def strip_selector():
	"""Create the strip selector component."""
	return html.Div([
		html.Div([
			html.Button('All', id='all-strip-button', style=SELECT_ALL_BUTTON),
			html.Button('None', id='no-strip-button', style=UNSELECT_ALL_BUTTON),
			html.Button("Even", id='even-strip-button', style=SELECT_BUTTON),
			html.Button("Odd", id='odd-strip-button', style=SELECT_BUTTON)
		], style=BUTTON_CONTAINER),
		
		html.Div([
			html.Div([
				dcc.Input(
					id='strip-search-input',
					type='text',
					placeholder='Search strips...',
					style=CUSTOM_DROPDOWN_INPUT,
					autoComplete='off'
				),
				html.Div('▼', style=DROPDOWN_ARROW)
			], id='strip-search-input-container', style=CUSTOM_DROPDOWN_INPUT_CONTAINER),
			html.Div(id='strip-dropdown-list'),
			html.Div(id='strip-dropdown-background')
		], style=CUSTOM_DROPDOWN_CONTAINER),

		html.Div(id='selected-strips-display', style=SELECTED_STRIPS_CONTAINER)
	]) 

def strip_store():
	"""Create the strip store component."""
	return dcc.Store(id='strip-store', data=[])

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

		html.Div(id='strips', style=SELECTED_STRIPS_CONTAINER),
		html.Div("No strip selected.", id='no-strip', style=NO_STRIP)
	]) 

def strip_store():
	"""Create the strip store component."""
	return dcc.Store(id='strip-store', data=[])

def strip(strip):
	return html.Div(
		strip,
		id={'type': 'strip-tag', 'index': strip},
		className='delete-button',
		style=SELECTED_STRIP_TAG
	)

def strip_option(strip):
	return html.Div(
		f'Strip {strip}',
		id={'type': 'select-strip', 'index': strip},
		className='strip-dropdown-item',
		style=CUSTOM_DROPDOWN_ITEM
	)

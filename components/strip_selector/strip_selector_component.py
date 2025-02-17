"""
This module contains the strip selector component.
"""
from dash import html, dcc
from .strip_selector_style import *

def StripSelector(file):
	"""Create the strip selector component."""
	return html.Div([
		html.Div([
			html.Button('All', id={'type': 'select-strips-button', 'file_id': file['id'], 'strips': 'all'}, className='button small success'),
			html.Button('None', id={'type': 'select-strips-button', 'file_id': file['id'], 'strips': 'none'}, className='button small danger'),
			html.Button("Even", id={'type': 'select-strips-button', 'file_id': file['id'], 'strips': 'even'}, className='button small info'),
			html.Button("Odd", id={'type': 'select-strips-button', 'file_id': file['id'], 'strips': 'odd'}, className='button small info')
		], style=BUTTON_CONTAINER),
		
		html.Div([
			html.Div([
				dcc.Input(
					id={'type': 'strip-search', 'file_id': file['id']},
					type='text',
					debounce=1,
					placeholder='Search strips...',
					style=CUSTOM_DROPDOWN_INPUT,
					autoComplete='off'
				),
				html.I(
					id={'type': 'strip-search-dropdown-icon', 'file_id': file['id']},
					className='fas fa-chevron-right',
					style=DROPDOWN_ARROW
				)
			], id={'type': 'strip-search-input', 'file_id': file['id']}, style=CUSTOM_DROPDOWN_INPUT_CONTAINER),
			html.Div(id={'type': 'strip-search-dropdown', 'file_id': file['id']}, style=HIDDEN),
			html.Div(id={'type': 'strip-search-overlay', 'file_id': file['id']}, style=HIDDEN)
		], style=CUSTOM_DROPDOWN_CONTAINER),

		html.Div(id={'type': 'selected-strips', 'file_id': file['id']}, style=SELECTED_STRIPS_CONTAINER),
		html.Div("No strip selected.", id={'type': 'no-selected-strip', 'file_id': file['id']}, className='muted'),
		
		dcc.Store(id={'type': 'selected-strips-store', 'file_id': file['id']}, data=[s for s in file['strips'].values() if s['selected']])
	], className='full-width')

def Strip(file, strip):
	return html.Div([
		html.Div(strip['id'], style=STRIP_LABEL),
		dcc.Input(
			id={'type': 'strip-noise', 'file_id': file['id'], 'strip_id': strip['id']},
			type='number',
			step=0.01,
			debounce=1,
			value=round(strip['noise'], 2),
			style=STRIP_NOISE
		),
	], id={'type': 'strip', 'file_id': file['id'], 'strip_id': strip['id']}, style=STRIP)

def SelectedStrip(file, strip):
	return html.Div(
		strip['id'],
		id={'type': 'selected-strip', 'file_id': file['id'], 'strip_id': strip['id']},
		className='button danger small inverted',
		style=SELECTED_STRIP_TAG
	)

def DropdownOption(file, strip):
	return html.Div(
		f'Strip {strip['id']}',
		id={'type': 'strip-search-option', 'file_id': file['id'], 'strip_id': strip['id']},
		className='strip-dropdown-item',
		style=CUSTOM_DROPDOWN_ITEM
	)

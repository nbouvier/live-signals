"""
This module contains the graph display component.
"""
from dash import html, dcc
from styles import *
from .file_selector_style import *

def file_selector():
	"""Create the file selector component."""
	return html.Div([
		# Add file button
		dcc.Upload(
			id='add-file',
			children=html.Button([
				html.I(className="fas fa-plus", style=BUTTON_ICON),
				"File"
			], className='button primary', style=ADD_FILE_BUTTON)
		),

		# Loaded files list
		html.Div(id='files', style=FILES_LIST),
		html.Div("No file loaded.", id='no-file', style=NO_FILE)
	])

def file_store():
	"""Create the file store component."""
	return dcc.Store(id='file-store', data={})

def file(file):
	"""Create the file component."""
	filename = file['filename'] if len(file['filename']) <= 15 else f"{file['filename'][0:15]}..."

	return html.Div([
		html.Div([
			# File name
			html.Div([
				html.I(className="fa-solid fa-file"),
				html.Span(filename, title=f'File {file['id']} : {filename}', style=FILE_NAME)
			], style=FILE_NAME_CONTAINER),

			# Offset input
			html.Div([
				html.Span("Offset (ms)", style=INPUT_LABEL),
				dcc.Input(
					id={'type': 'time-offset', 'index': file['id']},
					type='number',
					value=file['time_offset'],
					step=1000,
					debounce=True,
					style=INPUT
				)
			], style=INPUT_CONTAINER)
		], style=FILE_CARD_BODY),

		# Delete button
		html.Button(
			html.I(className="fas fa-trash"),
			id={'type': 'file-delete', 'index': file['id']},
			className='delete-button',
			style=FILE_DELETE
		)
	], id={'type': 'file-card', 'index': file['id']}, style=FILE_CARD)

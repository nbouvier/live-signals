from dash import html, dcc
from .styles import *

def StripManager(file):
	return html.Div([
		html.Div([
			"Strip noises",
			html.I(
				id={'type': 'toggle-strip-list-icon', 'file_id': file['id']},
				className='fas fa-chevron-right',
				style={'fontSize': FONT_SIZE_SMALL}
			)
		], id={'type': 'toggle-strip-list', 'file_id': file['id']}, style=STRIP_LIST_TOGGLE),

		html.Div([
			html.Div([
				Strip(file, s) for s in file['strips'].values()
			], id={'type': 'strip-list', 'file_id': file['id']}, style=STRIP_LIST),
			
			html.Div([
				html.Button('Update', id={'type': 'update-strip-noise-button', 'file_id': file['id'], 'action': 'update'}, className='button small info'),
				html.Button("Reset", id={'type': 'update-strip-noise-button', 'file_id': file['id'], 'action': 'reset'}, className='button small danger')
			], className='flex right small-gap'),
		], id={'type': 'strip-list-container', 'file_id': file['id']}, className='flex column small-gap', style=HIDDEN),

		dcc.Store(id={'type': 'strips-store', 'file_id': file['id']}, data=[s for s in file['strips'].values()])
	], className='flex column medium-gap full-width')

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

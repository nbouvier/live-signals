from dash import html, dcc
from .strip_noise_style import *

def StripNoise(file):
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
			Strip(file, s) for s in file['strips'].values()
		], id={'type': 'strip-list', 'file_id': file['id']}, style=HIDDEN)
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

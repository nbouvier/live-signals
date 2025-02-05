"""
This module contains the strip selector component.
"""
from dash import html, dcc
from .strip_selector_callbacks import register_callbacks
from .strip_selector_style import *

def create_strip_selector(app):
	"""Create the strip selector component."""

	register_callbacks(app)

	return html.Div([
		html.Div([
			html.H3('Strip Selection', style={'marginBottom': '10px'}),

			html.Div([
				html.Button(
					'Select All', 
					id='select-all-button',
					style=SELECT_ALL_BUTTON
				),
				html.Button(
					'Unselect All', 
					id='unselect-all-button',
					style=UNSELECT_ALL_BUTTON
				),
				html.Button(
					"Odd Strips",
					id='select-odd-button',
					style=SELECT_BUTTON
				),
				html.Button(
					"Even Strips",
					id='select-even-button',
					style=SELECT_BUTTON
				)
			], style=BUTTON_CONTAINER),
			dcc.Checklist(
				id='strip-selector',
				options=[
					{'label': f'Strip {i}', 'value': i} 
					for i in range(18, 153)
				],
				value=list(range(18, 153)),
				inline=True,
				labelStyle=STRIP_LABEL,
				style=STRIP_SELECTOR
			),
		], style={'position': 'relative'})
	], id='strip-selection-panel', style=OVERLAY) 

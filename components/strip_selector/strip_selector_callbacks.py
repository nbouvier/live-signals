"""
This module contains all the callback functions for the Dash application.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from models import CalculationResult, FileData

def register_strip_selector_callbacks(app):
	"""Register strip selector callbacks."""
	
	@app.callback(
		Output('strip-selector', 'value'),
		[Input('select-all-button', 'n_clicks'),
		 Input('unselect-all-button', 'n_clicks'),
		 Input('select-odd-button', 'n_clicks'),
		 Input('select-even-button', 'n_clicks')],
		[State('strip-selector', 'options')],
		prevent_initial_call=True
	)
	def update_strip_selection(select_clicks, unselect_clicks, odd_clicks, even_clicks, options):
		"""Update the strip selection when the buttons are clicked."""

		button_id = ctx.triggered[0]['prop_id'].split('.')[0]
		all_strips = [opt['value'] for opt in options]
		
		if button_id == 'select-all-button':
			return all_strips
		elif button_id == 'unselect-all-button':
			return []
		elif button_id == 'select-odd-button':
			return [strip for strip in all_strips if strip % 2 == 1]
		elif button_id == 'select-even-button':
			return [strip for strip in all_strips if strip % 2 == 0]
		
		return list(range(18, 153))  # Default case

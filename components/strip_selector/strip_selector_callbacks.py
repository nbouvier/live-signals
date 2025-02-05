"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from data_processing import create_figure, read_bin_file, process_file, create_multi_file_figure
from models import CalculationResult, FileData

def register_callbacks(app):
	"""Register strip selector callbacks."""

	@app.callback(
		[Output('strip-selection-panel', 'style', allow_duplicate=True),
		 Output('click-catcher', 'style', allow_duplicate=True),
		 Output('toggle-strip-selection', 'style', allow_duplicate=True)],
		[Input('toggle-strip-selection', 'n_clicks'),
		 Input('click-catcher', 'n_clicks')],
		[State('strip-selection-panel', 'style')],
		prevent_initial_call=True
	)
	def toggle_strip_selection(toggle_clicks, catcher_clicks, current_style):
		"""Toggle the strip selection panel visibility."""
		ctx = dash.callback_context

		# Initial state
		if not ctx.triggered:
			return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
		
		button_id = ctx.triggered[0]['prop_id'].split('.')[0]
		
		# Handle toggle button click
		if button_id == 'toggle-strip-selection':
			# If panel is hidden (or initial state), show it
			if not current_style or current_style == styles.OVERLAY:
				return styles.OVERLAY_VISIBLE, styles.CLICK_CATCHER, dict(styles.TOGGLE_BUTTON, **{'display': 'none'})
			# If panel is visible, hide it
			return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
			
		# Handle click catcher (clicking outside panel)
		elif button_id == 'click-catcher':
			return styles.OVERLAY, {'display': 'none'}, styles.TOGGLE_BUTTON
		
		# Default case: no change
		return dash.no_update, dash.no_update, dash.no_update

	@app.callback(
		Output('strip-selector', 'value'),
		[Input('select-all-button', 'n_clicks'),
		 Input('unselect-all-button', 'n_clicks'),
		 Input('select-odd-button', 'n_clicks'),
		 Input('select-even-button', 'n_clicks')],
		[State('strip-selector', 'options')]
	)
	def update_strip_selection(select_clicks, unselect_clicks, odd_clicks, even_clicks, options):
		ctx = dash.callback_context
		if not ctx.triggered:
			return list(range(18, 153))  # Default to all selected
		
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

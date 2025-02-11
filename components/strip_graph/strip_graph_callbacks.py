"""
This module contains all the callback functions for the strip graph.
"""

from dash import Input, Output, State, ctx, html, ALL, dcc, no_update
from .strip_graph_logic import create_strip_graph
from .strip_graph_style import *

def register_strip_graph_callbacks(app):
	"""Register strip graph callbacks."""
	
	@app.callback(
		[Output('strip-graph', 'figure'),
		 Output('strip-graph', 'style'),
		 Output('strip-graph-placeholder', 'style')],
		Input('average-store', 'data'),
		prevent_initial_call=True
	)
	def update_graph(averages):
		"""Update strip graph."""

		# Get plotted strips
		averages = [a for a in averages.values() if a['selected']]

		if not averages:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		strips = [s for s in averages[0]['strips'] if s['plot']]

		if not strips:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		# Create graph
		figure = create_strip_graph(strips)

		return figure, GRAPH, HIDDEN

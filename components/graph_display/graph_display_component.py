"""
This module contains the graph display component.
"""
from dash import html, dcc
from styles import *
from .graph_display_style import *

def graph_display():
	"""Create the graph display component."""
	return html.Div([
		dcc.Loading(
			id="loading-graph",
			type="default",
			delay_show=500,
			children=html.Div([
				# Graph
				dcc.Graph(
					id='strip-responses-graph',
					className='graph',
					style=HIDDEN
				),
				
				# Graph placeholder
				html.Div('No data to plot.', id='graph-placeholder', style=GRAPH_PLACEHOLDER)
			])
		)
	], className='graph-container', style=GRAPH_CONTAINER)

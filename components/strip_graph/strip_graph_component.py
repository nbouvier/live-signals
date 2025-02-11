"""
This module contains the strip graph component.
"""

from dash import html, dcc
from styles import *
from .strip_graph_style import *

def strip_graph():
	"""Create the exponential strip graph component."""	
	return html.Div([
		dcc.Loading(
			type="default",
			delay_show=500,
			children=html.Div([
				# Graph
				dcc.Graph(
					id="strip-graph",
					className='graph',
					style=HIDDEN
				),
				
				# Graph placeholder
				html.Div('No data to plot.', id='strip-graph-placeholder', style=GRAPH_PLACEHOLDER)
			])
		)
	], className='graph-container', style=GRAPH_CONTAINER) 

"""
This module contains the fit graph component.
"""

from dash import html, dcc
from styles import *
from .fit_graph_style import *

def fit_graph():
	"""Create the exponential fit graph component."""	
	return html.Div([
		dcc.Loading(
			type="default",
			delay_show=500,
			children=html.Div([
				# Graph
				dcc.Graph(
					id="fit-graph",
					className='graph',
					style=HIDDEN
				),
				
				# Graph placeholder
				html.Div('No data to plot.', id='fit-graph-placeholder', style=GRAPH_PLACEHOLDER)
			])
		)
	], className='graph-container', style=GRAPH_CONTAINER) 

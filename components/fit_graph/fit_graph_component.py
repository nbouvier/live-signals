"""
This module contains the fit graph component.
"""

from dash import html, dcc
from .fit_graph_logic import create_fit_graph
from .fit_graph_style import *

def fit_graph(app):
	"""Create the exponential fit graph component."""	
	return html.Div([
		html.Div(id='fit-graph-placeholder'),
		dcc.Graph(
			id="fit-graph",
			style=GRAPH
		)
	], id='fit-graph-container', style=CONTAINER) 

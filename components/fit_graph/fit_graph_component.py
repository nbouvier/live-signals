"""
This module contains the fit graph component.
"""
from dash import html, dcc
from .fit_graph_callbacks import register_callbacks
from .fit_graph_logic import create_fit_graph
from .fit_graph_style import *

def create_fit_graph(app, calculation_results):
    """Create the exponential fit graph component."""

    register_callbacks(app)
    
    return html.Div([
        dcc.Graph(
            figure=create_fit_graph(),
            style=GRAPH
        )
    ], style=CONTAINER) 

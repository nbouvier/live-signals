"""
This module contains the graph display component.
"""
from dash import html, dcc
from .graph_display_style import *  # Import styles directly from the style file

def create_graph_display(time_values, raw_strip_resp, create_figure):
    """Create the graph display component."""
    return html.Div([
        # Graph container
        html.Div([
            # Graph
            dcc.Loading(
                id="loading-graph",
                type="circle",
                children=dcc.Graph(
                    id='strip-responses-graph',
                    figure=create_figure(time_values, raw_strip_resp),
                    style=BASE_GRAPH
                )
            ),
            # Placeholder (same size as graph)
            html.Div(
                "No data to display. Please select at least one strip.",
                id='graph-placeholder',
                style=dict(BASE_PLACEHOLDER, **{'display': 'none'})
            )
        ], style=CONTAINER)
    ]) 
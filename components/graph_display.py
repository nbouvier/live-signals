"""
This module contains the graph display component.
"""
from dash import html, dcc
from styles import (
    BASE_GRAPH_STYLE,
    BASE_PLACEHOLDER_STYLE
)

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
                    style=BASE_GRAPH_STYLE
                )
            ),
            # Placeholder (same size as graph)
            html.Div(
                "No data to display. Please select at least one strip.",
                id='graph-placeholder',
                style=dict(BASE_PLACEHOLDER_STYLE, **{'display': 'none'})
            )
        ], style={'flex': '1 1 auto', 'minWidth': '0', 'width': '100%', 'position': 'relative'})
    ]) 
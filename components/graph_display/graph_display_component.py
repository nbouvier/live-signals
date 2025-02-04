"""
This module contains the graph display component.
"""
from dash import html, dcc
from .graph_display_style import *  # Import styles directly from the style file

def create_graph_display():
    """Create the graph display component."""
    return html.Div([
        # Graph container
        html.Div([
            # Graph (hidden initially)
            dcc.Loading(
                id="loading-graph",
                type="circle",
                children=dcc.Graph(
                    id='strip-responses-graph',
                    style=dict(BASE_GRAPH, **{'display': 'none'})
                )
            ),
            # Upload placeholder
            html.Div([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        html.I(className="fas fa-file-upload", style=UPLOAD_ICON),
                        html.Div('Drag and Drop or Click to Upload .bin File')
                    ]),
                    style=UPLOAD_BUTTON,
                    multiple=False
                )
            ], id='graph-placeholder', style=BASE_PLACEHOLDER)
        ], style=CONTAINER),
        
        # Loaded files section
        html.Div([
            html.Div(id='loaded-file-info', style=FILE_INFO)
        ], style=FILES_CONTAINER)
    ]) 

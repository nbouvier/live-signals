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
        
        # Files section
        html.Div([
            # Loaded files list
            html.Div(id='loaded-files-list', style=FILES_LIST),
            # Add file button
            dcc.Upload(
                id='add-file',
                children=html.Button([
                    html.I(className="fas fa-plus", style={'marginRight': '8px'}),
                    "Add File"
                ], style=ADD_FILE_BUTTON),
                style={'display': 'inline-block'}
            )
        ], style=FILES_CONTAINER)
    ]) 

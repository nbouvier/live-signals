"""
This module contains the layout of the application.
"""

from dash import html, dcc
import styles
from components.graph_display import create_graph_display
from components.strip_selector import create_strip_selector
from components.averages_panel import create_averages_panel
from components.fit_graph import create_fit_graph

def create_layout():
    """Create the application layout."""
    return html.Div([
        # URL Location component for page initialization
        dcc.Location(id='url', refresh=False),
        
        # Main content
        html.Div([
            # Graph display
            create_graph_display(),
            
            # Fit graph
            html.Div(id='fit-graph-container'),
            
            # Averages panel
            create_averages_panel()
        ], style=styles.MAIN_CONTENT),
        
        # Strip selection panel
        create_strip_selector(),
        
        # Click catcher for closing panels
        html.Div(id='click-catcher', style={'display': 'none'}),
        
        # Toggle button for strip selection
        html.Button([
            html.I(className="fas fa-bars", style={'marginRight': '8px'}),
            "Strip Selection"
        ], id='toggle-strip-selection', n_clicks=0, style=styles.TOGGLE_BUTTON),
        
        # Popup message
        html.Div([
            html.Div(id='popup-message-content'),
            html.Button(
                html.I(className="fas fa-times"),
                id='close-popup',
                style=styles.CLOSE_BUTTON
            )
        ], id='popup-message', style=styles.HIDDEN_POPUP)
    ]) 

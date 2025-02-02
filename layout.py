"""
This module contains the Dash layout components for the application.
"""

from dash import html
import styles
from components.strip_selector import create_strip_selector_panel
from components.graph_display import create_graph_display
from components.averages_panel import create_averages_panel
from components.popup_message import create_popup_message
from components.fit_graph import create_fit_graph

def create_layout(time_values, raw_strip_resp, create_figure):
    """Create the main application layout."""
    return html.Div([
        # Click catcher
        html.Div(id='click-catcher', style=dict(styles.CLICK_CATCHER, **{'display': 'none'})),
        
        # Popup message
        create_popup_message(),
        
        # Toggle button
        html.Button(
            '☰ Strip Selection', 
            id='toggle-strip-selection',
            style=styles.TOGGLE_BUTTON
        ),
        
        # Strip selection panel
        create_strip_selector_panel(),
        
        # Main content
        html.Div([
            # Flex container for graph and averages
            html.Div([
                create_graph_display(time_values, raw_strip_resp, create_figure),
                create_averages_panel()
            ], style={'display': 'flex', 'gap': '20px', 'width': '100%'}),
            
            # Fit graph container
            html.Div(id='fit-graph-container')
            
        ], style={'marginLeft': '60px', 'marginRight': '20px', 'width': 'calc(100% - 80px)'})]) 

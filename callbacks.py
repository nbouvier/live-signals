"""
This module contains all the callback functions for the Dash application.
"""

import numpy as np
from dash import Input, Output, State, ctx, html, ALL, dcc
import dash
import styles
from models import CalculationResult, FileData
from state import AppState

def register_callbacks(app):
    """Register all callbacks for the application."""
    
    @app.callback(
        [Output('strip-responses-graph', 'figure'),
         Output('strip-responses-graph', 'style'),
         Output('loaded-files-list', 'children'),
         Output('graph-placeholder', 'style'),
         Output('averages-content', 'children'),
         Output('fit-graph-container', 'children'),
         Output('strip-selection-panel', 'style')],
        Input('url', 'pathname')
    )
    def initialize_page(pathname):
        """Reset everything when the page loads."""
        AppState.reset()
        
        # Reset the display
        return (
            {},  # Empty figure
            dict(styles.BASE_GRAPH, **{'display': 'none'}),  # Hide graph
            None,  # Clear file info
            dict(styles.BASE_PLACEHOLDER, **{'display': 'block'}),  # Show upload placeholder
            None,  # Clear calculations
            None,  # Clear fit graph
            styles.OVERLAY  # Reset strip selection panel position
        )

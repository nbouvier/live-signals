"""
This module exports the graph display component.
"""

from .graph_display_callbacks import register_graph_display_callbacks
from .graph_display_component import graph_display

__all__ = ['graph_display', 'register_graph_display_callbacks']

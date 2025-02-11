"""
This module exports the strip graph component.
"""

from .strip_graph_callbacks import register_strip_graph_callbacks
from .strip_graph_component import strip_graph 

__all__ = ['strip_graph', 'register_strip_graph_callbacks']

"""
This module exports the averages panel component.
"""

from .averages_panel_callbacks import register_averages_panel_callbacks
from .averages_panel_component import averages_panel 

__all__ = ['averages_panel', 'register_averages_panel_callbacks']

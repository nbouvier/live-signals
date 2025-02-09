"""
This module exports the average component.
"""

from .average_callbacks import register_average_callbacks
from .average_component import average 

__all__ = ['average', 'register_average_callbacks']

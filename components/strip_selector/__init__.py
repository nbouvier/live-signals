"""
This module exports the strip selector component.
"""

from .strip_selector_callbacks import register_strip_selector_callbacks
from .strip_selector_component import strip_selector 

__all__ = ['strip_selector', 'register_strip_selector_callbacks']

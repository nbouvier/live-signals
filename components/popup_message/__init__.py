"""
This module exports the popup message component.
"""

from .popup_message_callbacks import register_popup_message_callbacks
from .popup_message_component import popup_message 

__all__ = ['popup_message', 'register_popup_message_callbacks']

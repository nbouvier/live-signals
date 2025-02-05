"""
This module exports the calculation result component.
"""

from .calculation_result_callbacks import register_calculation_result_callbacks
from .calculation_result_component import calculation_result 

__all__ = ['calculation_result', 'register_calculation_result_callbacks']

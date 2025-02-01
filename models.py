"""
This module contains data structures used in the application.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class CalculationResult:
    """
    Data structure to store calculation results.
    
    Attributes:
        overall_average: The overall average of the calculation
        thickness: The thickness value in millimeters (optional, integer)
    """
    overall_average: float
    thickness: Optional[int] = None 
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
        thickness: The thickness value in centimeters (optional, float with 2 decimal places)
    """
    overall_average: float
    thickness: Optional[float] = None 

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
        start_time: The start time of the selection range
        end_time: The end time of the selection range
        color: The color used to display this calculation in the graph
    """
    overall_average: float
    thickness: Optional[float] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    color: Optional[str] = None 

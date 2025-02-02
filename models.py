"""
This module contains data structures used in the application.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Tuple

@dataclass
class CalculationResult:
    """
    Data structure to store calculation results.
    
    Attributes:
        overall_average: The overall average of the calculation
        start_time: The start time of the selection range
        end_time: The end time of the selection range
        color: The color used to display this calculation in the graph
        strip_averages: List of tuples containing (strip_number, average_value)
        thickness: The thickness value in centimeters (optional, float with 2 decimal places)
    """
    # Required fields
    overall_average: float
    start_time: float
    end_time: float
    color: str
    strip_averages: List[Tuple[int, float]] = field(default_factory=list)
    
    # Optional fields
    thickness: Optional[float] = None
    
    # Auto-generated ID field
    id: int = field(init=False)
    
    # Class variable to keep track of the next ID (outside of dataclass fields)
    _next_id: int = 0
    
    def __post_init__(self):
        # Assign the next ID and increment it
        self.id = CalculationResult._next_id
        CalculationResult._next_id += 1
    
    @classmethod
    def reset_id_counter(cls):
        """Reset the ID counter back to 0."""
        cls._next_id = 0 

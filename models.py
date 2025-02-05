"""
This module contains data structures used in the application.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Tuple

@dataclass
class FileData:
	"""
	Data structure to store file data.
	
	Attributes:
		filename: Name of the uploaded file
		time_values: List of time values
		raw_strip_resp: 2D array of strip responses
		time_offset: Time offset in milliseconds
		id: Auto-generated unique identifier
	"""
	filename: str
	time_values: List[float]
	raw_strip_resp: List[List[float]]
	time_offset: float = 0
	
	# Auto-generated fields
	id: int = field(init=False)
	
	# Class variables
	_next_id = 0
	
	def __post_init__(self):
		# Assign the next ID and increment it
		self.id = FileData._next_id
		FileData._next_id += 1
	
	@classmethod
	def reset_id_counter(cls):
		"""Reset the ID counter back to 0."""
		cls._next_id = 0

@dataclass
class CalculationResult:
	"""
	Data structure to store calculation results.
	
	Attributes:
		overall_average: The overall average of the calculation
		start_time: The start time of the selection range
		end_time: The end time of the selection range
		strip_averages: List of tuples containing (strip_number, average_value)
		thickness: The thickness value in centimeters (optional, float with 2 decimal places)
	"""

	# Required fields
	overall_average: float
	start_time: float
	end_time: float
	strip_averages: List[Tuple[int, float]] = field(default_factory=list)
	
	# Optional fields
	thickness: Optional[float] = None
	
	# Auto-generated fields
	id: int = field(init=False)
	color: str = field(init=False)
	
	# Class variables (defined properly outside of dataclass fields)
	_next_id = 0
	_SELECTION_COLORS = [
		'rgba(128, 128, 128, 0.2)',  # Gray
		'rgba(100, 149, 237, 0.2)',  # Cornflower Blue
		'rgba(144, 238, 144, 0.2)',  # Light Green
		'rgba(255, 182, 193, 0.2)',  # Light Pink
		'rgba(255, 218, 185, 0.2)'   # Peach
	]
	
	def __post_init__(self):
		# Assign the next ID and increment it
		self.id = CalculationResult._next_id
		CalculationResult._next_id += 1
		
		# Assign color based on ID
		self.color = self._SELECTION_COLORS[self.id % len(self._SELECTION_COLORS)]
	
	@classmethod
	def reset_id_counter(cls):
		"""Reset the ID counter back to 0."""
		cls._next_id = 0 

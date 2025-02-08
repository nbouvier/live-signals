"""
This module contains data structures used in the application.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Tuple
import numpy as np

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

class CalculationResult:
	"""
	Data structure to store calculation results.
	
	Attributes:
		id: Auto-generated unique identifier
		color: Color assigned to this calculation result
		average: Average of strip responses
		strip_averages: List of strip averages
		start_time: The start time of the selection range
		end_time: The end time of the selection range
		thickness: The thickness value in centimeters (optional, float with 2 decimal places)
	"""
	# Class variables
	_next_id = 0
	_SELECTION_COLORS = [
		'rgba(128, 128, 128, 0.2)',  # Gray
		'rgba(100, 149, 237, 0.2)',  # Cornflower Blue
		'rgba(144, 238, 144, 0.2)',  # Light Green
		'rgba(255, 182, 193, 0.2)',  # Light Pink
		'rgba(255, 218, 185, 0.2)'   # Peach
	]

	def __init__(self, state, start_time: float, end_time: float, thickness: float = 1):
		"""
		Initialize a new CalculationResult.
		
		Args:
			start_time: The start time of the selection range
			end_time: The end time of the selection range
			thickness: The thickness value in centimeters (default: 1)
		"""
		# Required fields
		self.id = CalculationResult._next_id
		self.color = self._SELECTION_COLORS[self.id % len(self._SELECTION_COLORS)]
		self.average = 0.0
		self.strip_averages = []
		self.start_time = start_time
		self.end_time = end_time
		self.thickness = thickness
		
		# Auto-generated fields
		self.color = self._SELECTION_COLORS[self.id % len(self._SELECTION_COLORS)]
		CalculationResult._next_id += 1
		
		# Update calculations
		self.update(state)
	
	def update(self, state):
		"""Update calculations based on the current state."""

		# Calculate averages for each file
		self.strip_averages = []
		for file in state.loaded_files:
			# Adjust time range for this file's offset
			adjusted_start = self.start_time - file.time_offset
			adjusted_end = self.end_time - file.time_offset
			
			# Find indices in the adjusted time range
			start_idx = np.searchsorted(file.time_values, adjusted_start)
			end_idx = np.searchsorted(file.time_values, adjusted_end)
			
			# Skip if signal is not in range
			if start_idx == end_idx:
				continue
			
			# Calculate strip averages for this file
			file_strip_averages = []
			for strip_num in state.selected_strips:
				strip_avg = np.mean(file.raw_strip_resp[strip_num, start_idx:end_idx])
				file_strip_averages.append((strip_num, strip_avg))
			
			self.strip_averages.extend(file_strip_averages)
		
		# Calculate the overall average
		self.average = np.mean([avg for _, avg in self.strip_averages])
		
	@classmethod
	def reset_id_counter(cls):
		"""Reset the ID counter back to 0."""
		cls._next_id = 0

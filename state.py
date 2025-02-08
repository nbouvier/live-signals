from dataclasses import dataclass, field
from typing import List
from models import FileData, CalculationResult

@dataclass
class AppState:
	"""
	Data structure to store the application state.
	
	Attributes:
		loaded_files: List of FileData objects
		calculation_results: List of CalculationResult objects
		selected_strips: List of integers representing selected strip numbers
	"""    
	_instance = None
	
	loaded_files: List[FileData] = field(default_factory=list)
	calculation_results: List[CalculationResult] = field(default_factory=list)
	selected_strips: List[int] = field(default_factory=list)
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.loaded_files = []
			cls._instance.calculation_results = []
			cls._instance.selected_strips = []
		return cls._instance
	
	@classmethod
	def get_instance(cls):
		"""Get the singleton instance of AppState."""
		if cls._instance is None:
			cls._instance = cls()
		return cls._instance
	
	def reset(self):
		"""Reset the application state."""
		self.loaded_files.clear()
		FileData.reset_id_counter()
		
		self.calculation_results.clear()
		CalculationResult.reset_id_counter()
		
		self.selected_strips.clear()

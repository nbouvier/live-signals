from dataclasses import dataclass
from models import FileData, CalculationResult

@dataclass
class AppState:
	"""
	Data structure to store the application state.
	
	Attributes:
		loaded_files: List of FileData objects
		calculation_results: List of CalculationResult objects
	"""    
	# Class variables
	loaded_files = []  # 
	calculation_results = []
	
	@classmethod
	def reset(cls):
		"""Reset the application state."""
		cls.loaded_files.clear()
		FileData.reset_id_counter()
		
		cls.calculation_results.clear()
		CalculationResult.reset_id_counter()

import numpy as np
from stores import get_store_data

SELECTION_COLORS = [
	'rgba(128, 128, 128, 0.2)',  # Gray
	'rgba(100, 149, 237, 0.2)',  # Cornflower Blue
	'rgba(144, 238, 144, 0.2)',  # Light Green
	'rgba(255, 182, 193, 0.2)',  # Light Pink
	'rgba(255, 218, 185, 0.2)'   # Peach
]
	
average_id = 0

def update_average(stores, average):
	"""Update average."""

	files = get_store_data(stores, 'file-store')
	strips = get_store_data(stores, 'strip-store')

	# Calculate averages for each file
	average['strip_averages'] = []
	for file in files.values():
		# Adjust time range for this file's offset
		adjusted_start = average['start_time'] - file['time_offset']
		adjusted_end = average['end_time'] - file['time_offset']

		# Find indices in the adjusted time range
		start_idx = np.searchsorted(file['time_values'], adjusted_start)
		end_idx = np.searchsorted(file['time_values'], adjusted_end)
		
		# Skip if signal is not in range
		if start_idx == end_idx:
			continue
		
		# Calculate strip averages for this file
		file_strip_averages = []
		for strip in strips:
			strip_avg = np.mean(file['raw_strip_resp'][strip][start_idx:end_idx])
			file_strip_averages.append((strip, strip_avg))

		average['strip_averages'].extend(file_strip_averages)
	
	# Calculate the overall average
	average['average'] = np.mean([avg for _, avg in average['strip_averages']])

	return average

def process_average(stores, start_time, end_time):
	global average_id

	average_id += 1

	average = dict(
		id=average_id,
		color=SELECTION_COLORS[average_id % len(SELECTION_COLORS)],
		average=0.0,
		strip_averages=[],
		start_time=start_time,
		end_time=end_time,
		thickness=1
	)

	# Update average
	average = update_average(stores, average)

	return average

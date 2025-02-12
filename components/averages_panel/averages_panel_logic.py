import numpy as np
from stores import get_store_data

COLOR_PALETTE = [
	'rgba(249, 65, 68, #opacity#)',
	'rgba(144, 190, 109, #opacity#)',
	'rgba(249, 199, 79, #opacity#)',
	'rgba(39, 125, 161, #opacity#)',
	'rgba(243, 114, 44, #opacity#)',
	'rgba(67, 170, 139, #opacity#)',
	'rgba(249, 132, 74, #opacity#)',
	'rgba(87, 117, 144, #opacity#)',
	'rgba(248, 150, 30, #opacity#)',
	'rgba(77, 144, 142, #opacity#)'
]

COLOR_OPACITY = 1
SELECTED_COLOR_OPACITY = 0.5
UNSELECTED_COLOR_OPACITY = 0.2
	
average_id = 0

def update_average(stores, average):
	"""Update average."""

	files = get_store_data(stores, 'file-store')
	strips = get_store_data(stores, 'strip-store')
	
	file = files[str(average['file_id'])] if average['file_id'] else None
	offset = file['time_offset'] if file else 0

	# Calculate averages for each file
	average['strips'] = []
	for file in files.values():
		# Adjust time range for this file's offset
		adjusted_start = average['time_range'][0] + offset - file['time_offset']
		adjusted_end = average['time_range'][1] + offset - file['time_offset']

		# Find indices in the adjusted time range
		start_idx = np.searchsorted(file['time_values'], adjusted_start)
		end_idx = np.searchsorted(file['time_values'], adjusted_end)
		
		# Skip if signal is not in range
		if start_idx == end_idx:
			continue
		
		# Calculate strip averages for this file
		file_strips = []
		for strip_number in strips:
			strip = file['strips'][str(strip_number)]

			strip_average = np.mean([
				v for v in strip['noised_values'][start_idx:end_idx]
				if average['qdc_range'][0] <= v <= average['qdc_range'][1]
			])

			file_strips.append(dict(
				number=strip_number,
				file_id=file['id'],
				average=strip_average,
				plot=True
			))

		average['strips'].extend(file_strips)

	# Calculate the overall average
	average['average'] = np.mean([
		s['average'] for s in average['strips']
		if not np.isnan(s['average'])
	])

	return average

def process_average(stores, time_range, qdc_range, file_id=None, color=None):
	global average_id

	average_id += 1
	color = color or COLOR_PALETTE[average_id % len(COLOR_PALETTE)]

	average = dict(
		id=average_id,
		color=color.replace('#opacity#', str(COLOR_OPACITY)),
		selected_color=color.replace('#opacity#', str(SELECTED_COLOR_OPACITY)),
		unselected_color=color.replace('#opacity#', str(UNSELECTED_COLOR_OPACITY)),
		average=0.0,
		strips=[],
		time_range=time_range,
		qdc_range=qdc_range,
		thickness=1,
		selected=False,
		file_id=file_id
	)

	# Update average
	average = update_average(stores, average)

	return average

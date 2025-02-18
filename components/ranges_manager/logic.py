import numpy as np

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

def process_range(file, time_range, qdc_range, color=None):
	color = color or COLOR_PALETTE[file['next_range_id'] % len(COLOR_PALETTE)]

	range = dict(
		id=str(file['next_range_id']),
		color=color.replace('#opacity#', str(COLOR_OPACITY)),
		selected_color=color.replace('#opacity#', str(SELECTED_COLOR_OPACITY)),
		unselected_color=color.replace('#opacity#', str(UNSELECTED_COLOR_OPACITY)),
		average=np.nan,
		strips={},
		time_range=time_range,
		qdc_range=qdc_range,
		thickness=0,
		selected=False
	)

	file['next_range_id'] += 1

	return update_range(file, range)

def update_range(file, range):
	start_idx = np.searchsorted(file['time_values'], range['time_range'][0])
	end_idx = np.searchsorted(file['time_values'], range['time_range'][1])
	
	selected_strips = [s for s in file['strips'].values() if s['selected']]

	range['strips'] = {}
	for strip in selected_strips:
		range['strips'][strip['id']] = dict(
			id=strip['id'],
			average=np.mean([
				v for v in strip['values'][start_idx:end_idx]
				if range['qdc_range'][0] <= v <= range['qdc_range'][1]
			]),
			noised_average=np.mean([
				v for v in strip['noised_values'][start_idx:end_idx]
				if range['qdc_range'][0] <= v <= range['qdc_range'][1]
			])
		)

	range['average'] = np.mean([
		s['average'] for s in range['strips'].values()
		if not np.isnan(s['average'])
	])

	range['noised_average'] = np.mean([
		s['noised_average'] for s in range['strips'].values()
		if not np.isnan(s['noised_average'])
	])

	return range


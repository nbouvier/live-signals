import numpy as np

def process_strips(raw_strip_resp, time_values, noise_range):
	strips = {}

	for i, values in enumerate(raw_strip_resp):
		id = str(i + 1)

		noise_start = np.searchsorted(time_values, noise_range['time_range'][0])
		noise_end = np.searchsorted(time_values, noise_range['time_range'][1])

		noise = np.mean(values[noise_start:noise_end])

		strips[id] = update_strip(dict(
			id=id,
			values=values,
			noise=noise,
			noised_values=[],
			selected=False,
			filtered=False
		))

	return strips

def update_strip(strip):
	strip['noised_values'] = [v - strip['noise'] if strip['noise'] <= v else 0 for v in strip['values']]
	return strip

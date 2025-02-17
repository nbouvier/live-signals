import base64
import numpy as np
from pathlib import Path
from components.averages_panel import process_range
from components.strip_noise import process_strips

PLATEAU_DELTA = 0.01
PLATEAU_MIN_MATCHES = 10
BOX_SIZE_DELTA = 0.01

next_file_id = 0

def process_file(contents, filename):
	global next_file_id

	raw_strip_resp, time_values = read_bin_file(contents, filename)

	plateaus = find_plateaus(raw_strip_resp, time_values)
	noise_range = plateaus.pop(np.argmin([p['value'] for p in plateaus]))

	strips = process_strips(raw_strip_resp, time_values, noise_range)

	file = dict(
		id=str(next_file_id),
		filename=filename,
		time_values=time_values,
		time_offset=0,
		strips=strips,
		noise_range=noise_range,
		next_range_id=0,
		ranges={}
	)

	next_file_id += 1

	noises = [s['noise'] for s in strips.values()]
	for plateau in plateaus:
		noised_qdc_range = [plateau['qdc_range'][0] - max(noises), plateau['qdc_range'][1] - min(noises)]
		range = process_range(file, plateau['time_range'], noised_qdc_range)
		file['ranges'][range['id']] = range
	
	return file

def read_bin_file(contents, filename):
	content_type, content_string = contents.split(',')
	decoded = base64.b64decode(content_string)
	
	# Convert to numpy array
	dt = np.dtype("uint16")
	zdata = np.frombuffer(decoded, dt)

	# correspondence of QDC number and strip number file
	correspondence_table_path = Path(__file__).parent / "../../data/add_piste.txt"
	with correspondence_table_path.open("r") as file:
		correspondence_table = file.readlines()

	# number of measurements
	nb_mes = np.size(zdata) // 309

	# time conversion (integration time = 10 ms + 0.5 ms of dead time)
	time_values = [event * 10.5 for event in range(nb_mes)]

	# strips responses matrix (line = strips, columns = strip responses)
	raw_strip_resp = np.zeros((153, nb_mes))

	# 17 first strips on the missing diamond => 0 response
	for strip_num in range(18, 153):
		corresponding_QDC_num = int(correspondence_table[strip_num])
		for event in range(nb_mes):
			raw_strip_resp[strip_num, event] = np.uint32(
				((zdata[3 + corresponding_QDC_num * 2 + event * 309]) << 16)
				+ (zdata[4 + corresponding_QDC_num * 2 + event * 309])
				>> 6
			)

	return raw_strip_resp, time_values

def find_plateaus(raw_strip_resp, time_values):
	max_strip_resp = max([max(s) for s in raw_strip_resp])
	time_strips_mean = np.mean(raw_strip_resp, axis=0)

	# Init data
	plateaus = []
	evaluated_plateau = dict(
		start_time=time_values[0],
		end_time=time_values[0],
		response=time_strips_mean[0],
		matches=0
	)

	# Search for plateaus
	for mean, time in zip(time_strips_mean[1:], time_values[1:]):
		min_response = evaluated_plateau['response'] * (1 - PLATEAU_DELTA)
		max_response = evaluated_plateau['response'] * (1 + PLATEAU_DELTA)

		# If mean is in plateau, add to potential plateau
		if min_response <= mean <= max_response:
			evaluated_plateau['end_time'] = time
			evaluated_plateau['matches'] += 1
		
		# Else if plateau has reach minimum matches, add new plateau and reset postential plateau
		elif evaluated_plateau['matches'] >= PLATEAU_MIN_MATCHES:
			plateaus.append(dict(
				time_range=[evaluated_plateau['start_time'], evaluated_plateau['end_time']],
				qdc_range=[0, max_strip_resp * (1 + BOX_SIZE_DELTA)],
				value=evaluated_plateau['response']
			))
			evaluated_plateau = dict(
				start_time=time,
				end_time=time,
				response=mean,
				matches=1
			)

		# Else, reset potential plateau
		else:
			evaluated_plateau = dict(
				start_time=time,
				end_time=time,
				response=mean,
				matches=1
			)

	return plateaus

"""
This module contains functions for reading and processing binary data files.
"""

import base64
import numpy as np
from pathlib import Path

PLATEAU_DELTA = 0.01
PLATEAU_MIN_MATCHES = 10
BOX_SIZE_DELTA = 0.01

file_id = 0

def find_responses_plateaus(raw_strip_resp, time_values):
	max_strip_resp = max([max(s) for s in raw_strip_resp])
	time_strips_mean = np.mean(raw_strip_resp, axis=0)

	# Init data
	plateaus = []
	evaluated_range = dict(
		start_time=time_values[0],
		end_time=time_values[0],
		response=time_strips_mean[0],
		matches=0
	)

	# Search for plateaus
	for mean, time in zip(time_strips_mean[1:], time_values[1:]):
		min_response = evaluated_range['response'] * (1 - PLATEAU_DELTA)
		max_response = evaluated_range['response'] * (1 + PLATEAU_DELTA)

		# If mean is in plateau, dd to potential plateau
		if min_response <= mean <= max_response:
			evaluated_range['end_time'] = time
			evaluated_range['matches'] += 1
		
		# Else if plateau has reach minimum matches, add new plateau and reset postential plateau
		elif evaluated_range['matches'] >= PLATEAU_MIN_MATCHES:
			plateaus.append(dict(
				time_range=[evaluated_range['start_time'], evaluated_range['end_time']],
				qdc_range=[0, max_strip_resp * (1 + BOX_SIZE_DELTA)],
				base_value=evaluated_range['response']
			))
			evaluated_range = dict(
				start_time=time,
				end_time=time,
				response=mean,
				matches=1
			)

		# Else, reset potential plateau
		else:
			evaluated_range = dict(
				start_time=time,
				end_time=time,
				response=mean,
				matches=1
			)

	return plateaus
			

def process_file(contents, filename):
	"""Process uploaded bin file."""
	global file_id

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

	plateaus = find_responses_plateaus(raw_strip_resp, time_values)

	file_id += 1
	
	return dict(
		id=file_id,
		filename=filename,
		time_values=time_values,
		raw_strip_resp=raw_strip_resp,
		time_offset=0,
		ranges=plateaus
	)

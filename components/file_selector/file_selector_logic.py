"""
This module contains functions for reading and processing binary data files.
"""

import base64
import numpy as np
from models import FileData
from pathlib import Path

def process_file(contents, filename):
	"""Process uploaded file and return FileData object."""
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
	
	return FileData(filename, time_values, raw_strip_resp)

"""
This module contains functions for creating a graph.
"""

import plotly.graph_objects as go
from stores import get_store_data

def create_multi_file_figure(stores, strips):
	"""Create a figure with multiple files."""

	files = get_store_data(stores, 'file-store')
	averages = get_store_data(stores, 'average-store')

	fig = go.Figure()
	
	# Add traces for each file
	for strip in strips:
		for file in files.values():
			# Add time offset to each time value
			adjusted_time = [t + file['time_offset'] for t in file['time_values']]

			fig.add_scatter(
				x=adjusted_time,
				y=file['raw_strip_resp'][strip],
				name=f'Strip {strip} - File {file['id']}',
				mode='lines'
			)
	
	# Add rectangles for averages
	for average in averages.values():
		if average['start_time'] is not None and average['end_time'] is not None:
			# Get y-range for the rectangle
			y_min = min(min(strip) for strip in file['raw_strip_resp'] for file in files.values())
			y_max = max(max(strip) for strip in file['raw_strip_resp'] for file in files.values())
			delta = (y_max - y_min) * 0.05
			
			fig.add_shape(
				type="rect",
				x0=average['start_time'],
				x1=average['end_time'],
				y0=y_min - delta,
				y1=y_max + delta,
				fillcolor=average['color'],
				line=dict(width=0),
				layer="below"
			)

	# Update layout
	fig.update_layout(
		title=dict(
			text="Strip responses over time",
			font=dict(weight='bold', color='#666', size=20)
		),
		xaxis=dict(title=dict(text="Time (ms)", font=dict(weight='bold', color='#666'))),
		yaxis=dict(title=dict(text="Strip response (qdc)", font=dict(weight='bold', color='#666'))),
		hovermode='x unified',
		showlegend=True,
		height=400,
		dragmode='select',
		selectdirection='h'
	)
	
	return fig

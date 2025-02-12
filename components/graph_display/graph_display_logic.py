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
	noises = []
	for strip_number in strips:
		for file in files.values():
			strip = file['strips'][str(strip_number)]
			noises.append(strip['noise'])

			# Add time offset to each time value
			adjusted_time = [t + file['time_offset'] for t in file['time_values']]

			fig.add_scatter(
				x=adjusted_time,
				y=strip['noised_values'],
				name=f"Strip {strip['number']} (file {file['id']})",
				mode='lines',
				hovertemplate="%{y:.2f}"
			)

	# Add rectangles for averages
	for average in averages.values():
		file = files[str(average['file_id'])]
		offset = file['time_offset'] if file else 0
		
		fig.add_shape(
			type="rect",
			x0=average['time_range'][0] + offset,
			x1=average['time_range'][1] + offset,
			y0=average['qdc_range'][0] - max(noises),
			y1=average['qdc_range'][1] - min(noises),
			fillcolor=average['selected_color'] if average['selected'] else average['unselected_color'],
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
		showlegend=True,
		height=400,
		dragmode='select',
		selectdirection='h'
	)
	
	return fig

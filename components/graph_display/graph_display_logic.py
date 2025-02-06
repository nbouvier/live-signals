"""
This module contains functions for creating a graph.
"""

import plotly.graph_objects as go
from state import AppState

def create_multi_file_figure(selected_strips):
	"""Create a figure with multiple files."""
	state = AppState.get_instance()

	fig = go.Figure()
	
	# Add traces for each file, sorted by strip number
	traces = []
	# Sort selected strips numerically
	sorted_strips = sorted(selected_strips)
	
	for strip_num in sorted_strips:
		for file_data in state.loaded_files:
			# Add time offset to each time value
			adjusted_time = [t + file_data.time_offset for t in file_data.time_values]
			traces.append({
				'x': adjusted_time,
				'y': file_data.raw_strip_resp[strip_num, :],
				'name': f'Strip {strip_num} - File {file_data.id}',
				'mode': 'lines'
			})
	
	# Add traces in order (they're already sorted by strip number)
	for trace in traces:
		fig.add_scatter(**trace)
	
	# Add rectangles for calculations (if needed)
	if state.calculation_results:
		for result in state.calculation_results:
			if result.start_time is not None and result.end_time is not None:
				# Get y-range for the rectangle
				y_min = min(min(f.raw_strip_resp[sorted_strips, :].min() for f in state.loaded_files),
						  min(f.raw_strip_resp[sorted_strips, :].mean() for f in state.loaded_files))
				y_max = max(max(f.raw_strip_resp[sorted_strips, :].max() for f in state.loaded_files),
						  max(f.raw_strip_resp[sorted_strips, :].mean() for f in state.loaded_files))
				
				fig.add_shape(
					type="rect",
					x0=result.start_time,
					x1=result.end_time,
					y0=y_min,
					y1=y_max,
					fillcolor=result.color,
					line=dict(width=0),
					layer="below"
				)
	
	# Update layout
	fig.update_layout(
		title_x=0.5,
		xaxis=dict(
			title="Time (ms)",
			rangeselector=dict(
				buttons=list([
					dict(count=1, label="1s", step="second", stepmode="backward"),
					dict(count=5, label="5s", step="second", stepmode="backward"),
					dict(count=10, label="10s", step="second", stepmode="backward"),
					dict(step="all", label="All")
				])
			),
			domain=[0, 0.95]
		),
		yaxis_title="Strip response",
		hovermode='x unified',
		showlegend=True,
		legend=dict(
			x=1,
			y=1,
			xanchor='left',
			yanchor='top',
			traceorder='normal'  # Keep traces in the order they were added
		),
		height=800,
		dragmode='select',
		selectdirection='h',
		modebar=dict(
			remove=['lasso2d']
		),
		margin=dict(r=50)
	)
	
	return fig

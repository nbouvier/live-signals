import plotly.graph_objects as go

def strip_responses_figure(file):
	fig = go.Figure()

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
	
	# Add traces
	for strip in file['strips'].values():
		if not strip['selected']:
			continue

		fig.add_scatter(
			x=file['time_values'],
			y=strip['noised_values'],
			name=f"Strip {strip['id']}",
			mode='lines',
			hovertemplate="%{y:.2f}"
		)	

	# Add ranges
	for average in file['ranges'].values():
		fig.add_shape(
			type="rect",
			x0=average['time_range'][0],
			x1=average['time_range'][1],
			y0=average['qdc_range'][0],
			y1=average['qdc_range'][1],
			fillcolor=average['selected_color'] if average['selected'] else average['unselected_color'],
			line=dict(width=0),
			layer="below"
		)
	
	return fig

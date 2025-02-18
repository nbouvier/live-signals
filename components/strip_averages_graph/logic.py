import plotly.graph_objects as go

def create_strip_averages_graph(file, range):
	fig = go.Figure()
	
	fig.update_layout(
		title=dict(
			text=f'Strips average',
			font=dict(weight='bold', color='#666', size=20)
		),
		xaxis=dict(title=dict(text='Strip number', font=dict(weight='bold', color='#666'))),
		yaxis=dict(title=dict(text='Response average (qdc)', font=dict(weight='bold', color='#666'))),
		showlegend=True,
		height=400,
		dragmode='select'
	)
	
	fig.update_xaxes(tickformat=".0f")
	fig.update_yaxes(tickformat=".0f")
	
	for strip in range['strips'].values():
		if file['strips'][strip['id']]['selected']:
			fig.add_scatter(
				x=[strip['id']],
				y=[strip['noised_average']],
				name=f'Strip {strip['id']}',
				mode='markers',
				hovertemplate="%{y:.2f}"
			)

	return fig;

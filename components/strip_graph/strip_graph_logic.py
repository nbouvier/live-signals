from dash import html, dcc
import plotly.graph_objects as go
from .strip_graph_style import *

def create_strip_graph(strips):
	# Create the figure
	fig = go.Figure()
	
	# Add individual points with separate legends
	for strip in strips:
		fig.add_scatter(
			x=[strip['number']],
			y=[strip['average']],
			name=f'Strip {strip['number']} (file {strip["file_id"]})',
			mode='markers',
			hovertemplate="%{y:.2f}"
		)
	
	# Update layout
	fig.update_layout(
		title=dict(
			text=f'Strips average',
			font=dict(weight='bold', color='#666', size=20)
		),
		xaxis=dict(title=dict(text='Strip number', font=dict(weight='bold', color='#666'))),
		yaxis=dict(title=dict(text='Response average (qdc)', font=dict(weight='bold', color='#666'))),
		showlegend=False,
		height=400,
		width=400,
		modebar_remove=['select2d', 'lasso2d']
	)
	
	# Update axes to show 2 decimal places for x and 0 decimal places for y
	fig.update_xaxes(tickformat=".0f")
	fig.update_yaxes(tickformat=".0f")

	return fig;

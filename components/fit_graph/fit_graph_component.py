from dash import html, dcc
from styles import *

def exponential_fit_graph():
	return html.Div([
		dcc.Loading(
			type="default",
			delay_show=500,
			children=html.Div([
				dcc.Graph(
					id="exponential-fit-graph",
					className='graph',
					config={'scrollZoom': True, 'displaylogo': False},
					style=HIDDEN
				),
				
				html.Div('No data to plot.', id='exponential-fit-graph-placeholder', style=GRAPH_PLACEHOLDER)
			])
		)
	], className='graph-container', style=GRAPH_CONTAINER) 

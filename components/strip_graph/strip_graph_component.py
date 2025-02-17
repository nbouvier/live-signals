from dash import html, dcc
from styles import *

def StripAveragesGraph(file):
	return html.Div([
		dcc.Loading(
			type="default",
			delay_show=500,
			children=html.Div([
				dcc.Graph(
					id={'type': 'strip-averages-graph', 'file_id': file['id']},
					className='graph',
					config={'scrollZoom': True, 'displaylogo': False},
					style=HIDDEN
				),
				
				html.Div(
					'No data to plot.',
					id={'type': 'strip-averages-graph-placeholder', 'file_id': file['id']},
					style=GRAPH_PLACEHOLDER
				)
			])
		)
	], id={'type': 'strip-averages-graph-container', 'file_id': file['id']}, style=TAB_GRAPH_CONTAINER) 

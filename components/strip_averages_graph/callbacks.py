from dash import Input, Output, State, MATCH, no_update
from styles import *
from .logic import create_strip_averages_graph

def register_strip_averages_graph_callbacks(app):
	
	@app.callback(
		[Output({'type': 'strip-averages-graph', 'file_id': MATCH}, 'figure'),
		 Output({'type': 'strip-averages-graph', 'file_id': MATCH}, 'style'),
		 Output({'type': 'strip-averages-graph-placeholder', 'file_id': MATCH}, 'style')],
		[Input({'type': 'ranges-store', 'file_id': MATCH}, 'data'),
		 Input({'type': 'selected-strips-store', 'file_id': MATCH}, 'data')],
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def update_strip_averages_graph(_ranges, strips, file):
		if not strips:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		selected_range = None

		for range in file['ranges'].values():
			if range['selected']:
				selected_range = range
				break

		if not selected_range:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER
		
		return create_strip_averages_graph(selected_range), GRAPH, HIDDEN

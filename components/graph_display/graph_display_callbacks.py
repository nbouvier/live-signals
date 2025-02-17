from dash import Input, Output, State, MATCH, no_update
from styles import *
from .graph_display_logic import strip_responses_figure

def register_strip_responses_graph_callbacks(app):

	@app.callback(
		[Output({'type': 'strip-responses-graph', 'file_id': MATCH}, 'figure'),
		 Output({'type': 'strip-responses-graph', 'file_id': MATCH}, 'style'),
		 Output({'type': 'strip-responses-graph-placeholder', 'file_id': MATCH}, 'style')],
		[Input({'type': 'ranges-store', 'file_id': MATCH}, 'data'),
		 Input({'type': 'strips-store', 'file_id': MATCH}, 'data')],
		State({'type': 'file-store', 'file_id': MATCH}, 'data')
	)
	def update_strip_responses_graph(_ranges, strips, file):
		if not strips:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		return strip_responses_figure(file), GRAPH, HIDDEN

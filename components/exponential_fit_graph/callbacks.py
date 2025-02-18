import numpy as np
from dash import Input, Output, State, ALL, no_update
from styles import *
from .logic import exponential_fit_figure, calc_mu, exponential_model

def register_exponential_fit_graph_callbacks(app):
	
	@app.callback(
		[Output('exponential-fit-graph', 'figure'),
		 Output('exponential-fit-graph', 'style'),
		 Output('exponential-fit-graph-placeholder', 'style')],
		Input({'type': 'ranges-store', 'file_id': ALL}, 'data'),
		State({'type': 'file-store', 'file_id': ALL}, 'data'),
		prevent_initial_call=True
	)
	def update_exponential_fit_graph(_ranges, files):
		ranges = [
			r for f in files for r in f['ranges'].values()
			if r['noised_average'] is not None and r['thickness'] is not None
		]
		
		if len(ranges) < 2:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		x = [a['thickness'] for a in ranges]
		y = [a['noised_average'] for a in ranges]

		a, b = calc_mu(x, y)

		if a is None or b is None:
			return no_update, HIDDEN, GRAPH_PLACEHOLDER

		x_fit = np.linspace(0, max(x), 100)
		y_fit = exponential_model(x_fit, a, b)

		return exponential_fit_figure(x, y, x_fit, y_fit, b), GRAPH, HIDDEN

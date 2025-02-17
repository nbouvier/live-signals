from dash import Input, Output, ALL
from styles import *

def register_callbacks(app):
	
	@app.callback(
		[Output('side-panel', 'style'),
		 Output({'type': 'toggle-side-panel-icon', 'id': ALL}, 'className')],
		Input('toggle-side-panel', 'n_clicks'),
		prevent_initial_call=True
	)
	def toggle_side_panel(clicks):
		style = SIDE_PANEL if clicks % 2 == 0 else HIDDEN
		classes = "fas fa-chevron-left" if clicks % 2 == 0 else "fas fa-chevron-right"

		return style, [classes, classes]

from dash import html, dcc
from styles import *
from callbacks import register_callbacks
from components.ranges_manager import register_ranges_manager_callbacks
from components.files_manager import FileManager, register_files_manager_callbacks
from components.exponential_fit_graph import ExponentialFitGraph, register_exponential_fit_graph_callbacks
from components.strip_responses_graph import register_strip_responses_graph_callbacks
from components.popup_manager import PopupList, register_popup_manager_callbacks
from components.strip_averages_graph import register_strip_averages_graph_callbacks
from components.strip_manager import register_strips_manager_callbacks
from components.strip_selector import register_strip_selector_callbacks

def create_layout(app):
	register_callbacks(app)
	register_ranges_manager_callbacks(app)
	register_exponential_fit_graph_callbacks(app)
	register_files_manager_callbacks(app)
	register_popup_manager_callbacks(app)
	register_strip_averages_graph_callbacks(app)
	register_strip_responses_graph_callbacks(app)
	register_strips_manager_callbacks(app)
	register_strip_selector_callbacks(app)

	return html.Div([
		# Left panel
		html.Div(FileManager(), id='side-panel', style=SIDE_PANEL),
		html.Div([
			html.Div([
				html.I(id={'type': 'toggle-side-panel-icon', 'id': 1}, className="fas fa-chevron-left"),
				html.I(id={'type': 'toggle-side-panel-icon', 'id': 2}, className="fas fa-chevron-left")
			], id='toggle-side-panel', style=TOGGLE_SIDE_PANEL)
		], id='toggle-side-panel-container', style=TOGGLE_SIDE_PANEL_CONTAINER),

		# Center panel
		html.Div([
			html.Div([], id='graphs', className='flex medium-gap', style=GRAPHS_CONTAINER),
			ExponentialFitGraph()
		], style=CENTER_PANEL),
		
		PopupList()
	], style=MAIN_CONTAINER)

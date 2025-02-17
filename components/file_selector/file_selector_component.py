from dash import html, dcc
from styles import *
from components.averages_panel import RangeSelector
from components.strip_selector import StripSelector
from components.graph_display import StripResponsesGraph
from components.strip_graph import StripAveragesGraph
from components.strip_noise import StripNoise
from .file_selector_style import *

def FileSelector():
	return html.Div([
		dcc.Upload(
			id='add-file',
			children=html.Button(
				[html.I(className="fas fa-plus"), "File" ],
				className='button info big'
			)
		),

		html.Div(FilesPlaceholder(), id='files', className='flex column')
	], className='flex column medium-gap')

def FilesPlaceholder():
	return html.Div("No file loaded.", id='files-placeholder', className='text-medium muted')

def File(file):
	filename = file['filename'] if len(file['filename']) <= 30 else f"{file['filename'][0:30]}..."

	return html.Div([
		html.Div([
			html.Div([
				html.I(className="fa-solid fa-file"),
				html.Span(filename, title=filename, style=FILE_NAME)
			]),
			html.I(id={'type': 'file-header-toggle', 'file_id': file['id']}, className="fas fa-chevron-down")
		], id={'type': 'file-header', 'file_id': file['id']}, style=FILE_HEADER),

		html.Div([
			StripNoise(file),
			StripSelector(file),
			RangeSelector(file),

			html.Button(
				"Delete",
				id={'type': 'delete-file', 'file_id': file['id']},
				className='button danger big'
			)
		], id={'type': 'file-body', 'file_id': file['id']}, style=FILE_BODY),

		dcc.Store(id={'type': 'file-store', 'file_id': file['id']}, data=file)
	], id={'type': 'file', 'file_id': file['id']}, style=FILE)

def FileGraphs(file):
	return html.Div([
		dcc.Tabs([
			dcc.Tab(
				label="Responses", value="responses",
				children=StripResponsesGraph(file),
				style=TAB, selected_style=SELECTED_TAB
			),

			dcc.Tab(
				label="Averages", value="averages",
				children=StripAveragesGraph(file),
				style=TAB, selected_style=SELECTED_TAB
			)
		], value="responses")
	], id={'type': 'file_graphs', 'file_id': file['id']}, style=FILE_GRAPHS_CONTAINER)

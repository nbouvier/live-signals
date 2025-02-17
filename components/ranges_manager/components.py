from dash import html, dcc
from styles import *
from .styles import *

def RangeManager(file):
	return html.Div([
		html.Button(
			[html.I(className="fas fa-plus"), "Range" ],
			id={'type': 'add-range', 'file_id': file['id']},
			className='button info big'
		),
		
		html.Div(RangesPlaceholder(file), id={'type': 'ranges', 'file_id': file['id']}, style=AVERAGES_CONTENT),

		dcc.Store(id={'type': 'ranges-store', 'file_id': file['id']}, data=list(file['ranges'].keys()))
	], className='flex column medium-gap full-width')

def RangesPlaceholder(file):
	return html.Div("No range calculated.", id={'type': 'no-range', 'file_id': file['id']}, className='text-small muted')

def Range(file, range):
	return html.Div([
		html.Div([
			html.Div([
				html.Div([
					# Colored box and average value
					html.Div([
						html.Div(style={**COLOR_BOX, 'backgroundColor': range['color']}),
						html.Span(
							f"{range['average']:.2f}" if range['average'] is not None else 'N/A',
							style={'fontSize': '16px', 'fontWeight': 'bold'}
						),
						html.Span("qdc", style={'fontSize': '12px', 'fontWeight': 'bold', 'marginLeft': '2px'})
					], style={'display': 'flex', 'alignItems': 'center'}),

					# Time range
					html.Span(
						f"{range['time_range'][0]:.1f}ms - {range['time_range'][1]:.1f}ms",
						style=TIME_RANGE
					)
				]),

				# Thickness input
				html.Div([
					html.Span("Thickness (cm)", style=INPUT_LABEL),
					dcc.Input(
						id={'type': 'thickness-input', 'file_id': file['id'], 'range_id': range['id']},
						type='number',
						value=range['thickness'],
						step=0.01,
						debounce=1,
						style=INPUT
					)
				], style=INPUT_CONTAINER)
			], style=HEADER),
			
			# Collapsible section for individual strip averages
			html.Div([
				# Title
				html.Div([
						html.I(
							id={'type': 'strip-averages-toggle-icon', 'file_id': file['id'], 'range_id': range['id']},
							className="fas fa-chevron-right"
						),
						"Individual Strip Averages"
					],
					id={'type': 'strip-averages-toggle', 'file_id': file['id'], 'range_id': range['id']},
					style=INDIVIDUAL_AVERAGES_BUTTON
				),

				# Content
				html.Div(
					[IndivudualStrip(s) for s in range['strips'].values()],
					id={'type': 'strip-averages-content', 'file_id': file['id'], 'range_id': range['id']},
					style=HIDDEN
				)
			])
		], style={'padding': '12px 16px 12px 12px', 'flex': 1}),

		html.Div([
			# Select button
			html.Button(
				html.I(className="fas fa-eye"),
				id={'type': 'select-range', 'file_id': file['id'], 'range_id': range['id']},
				className=f"button secondary inverted no-growth {'active' if range['selected'] else ''}",
				style=SELECT_BUTTON
			),

			# Delete button
			html.Button(
				html.I(className="fas fa-trash"),
				id={'type': 'delete-range', 'file_id': file['id'], 'range_id': range['id']},
				className='button danger inverted no-growth',
				style=DELETE_BUTTON
			)
		], style=BUTTON_CONTAINER)
	], id={'type': 'range', 'file_id': file['id'], 'range_id': range['id']}, style=CONTAINER)

def IndivudualStrip(strip):
	average = f"{strip['average']:.2f}" if strip['average'] is not None else 'N/A'

	return html.Div([
		html.Div(strip['id'], style={'display': 'flex', 'justifyContent': 'center', 'fontWeight': 'bold', 'minWidth': '28px'}),
		html.Span('-', style={'fontWeight': 'bold', 'marginTop': '-2px'}),
		html.Span(average, style={'margin': '0px 4px'}),
		html.Span('qdc', style={'fontSize': '10px'})
	], style=STRIP_AVERAGE_ITEM)


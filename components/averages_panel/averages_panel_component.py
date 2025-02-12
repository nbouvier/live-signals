"""
This module contains the averages panel component.
"""
from dash import html, dcc
from styles import *
from .averages_panel_style import *

def averages_panel():
	"""Create the averages panel component."""
	return html.Div([
		html.Button([
			html.I(className="fas fa-plus", style=BUTTON_ICON),
			"Average"
		], id='add-average', className='button primary', style=CALCULATE_BUTTON),
		
		html.Div(id='averages', style=AVERAGES_CONTENT),
		html.Div("No average calculated.", id='no-average', style=NO_AVERAGE)
	])

def average_store():
	"""Create the average store component."""
	return dcc.Store(id='average-store', data={})

def average(average):
	"""Create an average component."""
	average_average = f"{average['average']:.2f}" if average['average'] is not None else 'N/A'

	return html.Div([
		html.Div([
			# Header with overall average and delete button
			html.Div([
				# Left side with overall average
				html.Div([
					html.Div([
						html.Div(style={**COLOR_BOX, 'backgroundColor': average['color']}),
						html.Span(average_average, style={'fontSize': '16px', 'fontWeight': 'bold'}),
						html.Span("qdc", style={'fontSize': '12px', 'fontWeight': 'bold', 'marginLeft': '2px'})
					], style={'display': 'flex', 'alignItems': 'center'}),

					# Time range subtitle with color indicator
					html.Span(
						f"{average['time_range'][0]:.1f}ms - {average['time_range'][1]:.1f}ms",
						style=TIME_RANGE
					)
				]),

				# Thickness input
				html.Div([
					html.Span("Thickness (cm)", style=INPUT_LABEL),
					dcc.Input(
						id={'type': 'thickness-input', 'index': average['id']},
						type='number',
						value=average['thickness'],
						step=0.01,
						debounce=True,
						style=INPUT
					)
				], style=INPUT_CONTAINER)
			], style=HEADER),
			
			# Collapsible section for individual averages
			html.Div([
				html.Div([
					# Toggle button with arrow
					html.Button([
							html.I(className="fas fa-chevron-right", style=TOGGLE_ICON),
							html.Span("Individual Strip Averages", style={'color': '#666', 'fontSize': '12px'})
						],
						id={'type': 'toggle-strip-averages', 'index': average['id']},
						style=INDIVIDUAL_AVERAGES_BUTTON
					)
				]),

				# Content
				html.Div([strip_average(s) for s in average['strips']],
					id={'type': 'strip-averages-content', 'index': average['id']},
					style=STRIP_AVERAGES_CONTENT
				)
			])
		], style={'padding': '12px 16px 12px 12px', 'flex': 1}),

		html.Div([
			# Select button
			html.Button(
				html.I(className="fas fa-eye"),
				id={'type': 'select-average', 'index': average['id']},
				className=f"info-button {'active' if average['selected'] else ''}",
				style=SELECT_BUTTON
			),

			# Delete button
			html.Button(
				html.I(className="fas fa-trash"),
				id={'type': 'delete-average', 'index': average['id']},
				className='delete-button',
				style=DELETE_BUTTON
			)
		], style=BUTTON_CONTAINER)
	], id={'type': 'average', 'index': average['id']}, style=CONTAINER)

def strip_average(strip):
	"""Create an individual strip average component."""

	average = f"{strip['average']:.2f}" if strip['average'] is not None else 'N/A'

	return html.Div(f"Strip {strip['number']} (file {strip['file_id']}): {average} qdc", style=STRIP_AVERAGE_ITEM)


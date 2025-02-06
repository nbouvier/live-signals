"""
This module contains the calculation result component.
"""
from dash import html, dcc
from .calculation_result_style import *


def calculation_result(app, calculation_result):
	"""
	Create a calculation result component.
	
	Args:
		calculation_result: The CalculationResult object containing all the data
	"""
	# Make the color more opaque for the indicator
	opaque_color = calculation_result.color.replace('0.2)', '0.8)')
	
	return html.Div([
		html.Div([
			# Header with overall average and delete button
			html.Div([
				# Left side with overall average
				html.Div([
					html.Div([
						html.Span(
							f"{calculation_result.overall_average:.2f}",
							style={'fontSize': '16px', 'fontWeight': 'bold'}
						),
						html.Span("qdc", style={'fontSize': '12px', 'fontWeight': 'bold', 'marginLeft': '2px'}),
						html.Div(style={
							'width': '12px',
							'height': '12px',
							'backgroundColor': opaque_color,
							'marginTop': '-2px',
							'marginLeft': '10px',
							'display': 'inline-block',
							'verticalAlign': 'middle',
							'borderRadius': '2px'
						})
					], style={'display': 'flex', 'alignItems': 'center'}),

					# Time range subtitle with color indicator
					html.Span(
						f"{calculation_result.start_time:.1f}ms - {calculation_result.end_time:.1f}ms",
						style=TIME_RANGE
					)
				]),

				# Thickness input
				html.Div([
					html.Span("Thickness: ", style={'fontSize': '10px', 'fontWeight': 'bold', 'color': '#666'}),
					dcc.Input(
						id={'type': 'thickness-input', 'index': calculation_result.id},
						type='number',
						placeholder='...',
						value=calculation_result.thickness,
						step=0.01,
						style=THICKNESS_INPUT
					)
				], style=THICKNESS_CONTAINER)
			], style=HEADER),
			
			# Collapsible section for individual averages
			html.Div([
				# Toggle button with arrow
				html.Button([
						html.I(className="fas fa-chevron-right", style=TOGGLE_ICON),
						html.Span("Individual Strip Averages", style={'color': '#666', 'fontSize': '12px'})
					],
					id={'type': 'toggle-strip-averages', 'index': calculation_result.id},
					style=INDIVIDUAL_AVERAGES_BUTTON
				),

				# Content (hidden by default)
				html.Div([
						html.Div(f"Strip {strip_num}: {avg:.2f}", 
								style=AVERAGE_ITEM)
						for strip_num, avg in sorted(calculation_result.strip_averages)
					],
					id={'type': 'strip-averages-content', 'index': calculation_result.id},
					style=AVERAGES_CONTENT
				)
			])
		], style={'padding': '12px 16px 12px 12px', 'flex': 1}),

		# Delete button
		html.Button(
			html.I(className="fas fa-trash"),
			id={'type': 'delete-calculation', 'index': calculation_result.id},
			className='delete-average-button',
			style={
				'border': '1px solid #dc3545',
				'borderTopRightRadius': '4px',
				'borderBottomRightRadius': '4px',
				'backgroundColor': 'transparent',
				'color': '#dc3545',
				'width': '32px',
				'padding': '4px',
				'cursor': 'pointer',
				'transition': 'all 0.3s',
				':hover': {
					'backgroundColor': '#dc3545',
					'color': 'white'
				}
			}
		)
	], style=CONTAINER) 

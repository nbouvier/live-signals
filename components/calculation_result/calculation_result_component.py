"""
This module contains the calculation result component.
"""
from dash import html, dcc
from .calculation_result_callbacks import register_callbacks
from .calculation_result_style import *


def create_calculation_result(app, calculation_result):
	"""
	Create a calculation result component.
	
	Args:
		calculation_result: The CalculationResult object containing all the data
	"""

	register_callbacks(app)

	# Make the color more opaque for the indicator
	opaque_color = calculation_result.color.replace('0.2)', '0.8)')
	
	return html.Div([
		# Header with overall average and delete button
		html.Div([
			# Left side with overall average
			html.Div([
				html.Div([
					html.Span("Average ", style={'fontSize': '20px', 'fontWeight': 'bold'}),
					html.Span(f"{calculation_result.overall_average:.2f}", 
							  style={'fontSize': '20px', 'marginLeft': '4px', 'fontWeight': 'bold'})
				]),

				# Color indicator square
				html.Div(style={
					'width': '12px',
					'height': '12px',
					'backgroundColor': opaque_color,
					'marginLeft': '8px',
					'display': 'inline-block',
					'verticalAlign': 'middle'
				})
			], style={'display': 'flex', 'alignItems': 'center'}),
			
			# Delete button
			html.Button(
				html.I(className="fas fa-trash"),
				id={'type': 'delete-calculation', 'index': calculation_result.id},
				style={
					'border': '1px solid #dc3545',
					'borderRadius': '4px',
					'backgroundColor': 'transparent',
					'color': '#dc3545',
					'width': '32px',
					'height': '32px',
					'padding': '4px',
					'cursor': 'pointer',
					'transition': 'all 0.3s',
					':hover': {
						'backgroundColor': '#dc3545',
						'color': 'white'
					}
				}
			)
		], style=HEADER),

		# Time range subtitle with color indicator
		html.Div([
			html.Span(
				f"{calculation_result.start_time:.1f}ms - {calculation_result.end_time:.1f}ms",
				style={'color': '#666', 'fontSize': '14px'}
			)
		], style=TIME_RANGE),
		
		# Thickness input
		html.Div([
			html.Strong("Thickness: ", style={'color': '#666'}),
			dcc.Input(
				id={'type': 'thickness-input', 'index': calculation_result.id},
				type='number',
				placeholder='Enter thickness...',
				value=calculation_result.thickness,
				step=0.01,
				style=THICKNESS_INPUT
			),
			html.Span("cm", style=UNIT_LABEL)
		], style=SECTION),
		
		# Collapsible section for individual averages
		html.Div([
			# Toggle button with arrow
			html.Button([
				html.I(className="fas fa-chevron-right", style=TOGGLE_ICON),
				html.Strong("Individual Strip Averages", style={'color': '#666'})
			],
			id={'type': 'toggle-strip-averages', 'index': calculation_result.id},
			style=TOGGLE_BUTTON),
			# Content (hidden by default)
			html.Div([
				html.Div(f"Strip {strip_num}: {avg:.2f}", 
						style=AVERAGE_ITEM)
				for strip_num, avg in sorted(calculation_result.strip_averages)
			],
			id={'type': 'strip-averages-content', 'index': calculation_result.id},
			style=AVERAGES_CONTENT)
		])
	], style=CONTAINER) 

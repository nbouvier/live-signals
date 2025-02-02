"""
This module contains the calculation result component.
"""
from dash import html, dcc
from .calculation_result_style import *  # Import styles directly from the style file
from data_processing import SELECTION_COLORS  # Import the colors

def create_calculation_result(calculation_result):
    """
    Create a calculation result component.
    
    Args:
        calculation_result: The CalculationResult object containing all the data
    """
    # Make the color more opaque for the indicator
    opaque_color = calculation_result.color.replace('0.2)', '0.8)')
    
    return html.Div([
        html.Hr(style=DIVIDER),
        html.Div([
            # Left side with color indicator and title
            html.Div([
                html.Div(style={
                    'width': '20px',
                    'height': '20px',
                    'backgroundColor': opaque_color,
                    'borderRadius': '50%',
                    'display': 'inline-block',
                    'marginRight': '10px',
                    'verticalAlign': 'middle'
                }),
                html.Strong("Time Range: "),
                html.Span(f"{calculation_result.start_time:.1f}ms - {calculation_result.end_time:.1f}ms", 
                         style={'color': '#666'})
            ], style={'display': 'inline-block'}),
            # Delete button on the right
            html.Button(
                html.I(className="fas fa-trash", style={'color': '#dc3545'}),
                id={'type': 'delete-calculation', 'index': calculation_result.id},
                style={
                    'float': 'right',
                    'border': 'none',
                    'background': 'none',
                    'cursor': 'pointer',
                    'padding': '5px',
                    'marginTop': '-5px'
                }
            )
        ], style=HEADER),
        html.Div([
            html.Strong("Overall Average: "),
            html.Span(f"{calculation_result.overall_average:.2f}", 
                     id={'type': 'overall-average', 'index': calculation_result.id})
        ], style=SECTION),
        html.Div([
            html.Strong("Thickness: "),
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
                html.Strong("Individual Strip Averages")
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

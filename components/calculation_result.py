"""
This module contains the calculation result component.
"""
from dash import html
import styles

def create_calculation_result(current_calcs, start_time, end_time, overall_avg, strip_averages):
    """Create a calculation result component."""
    return html.Div([
        html.Hr(style={'margin': '20px 0'}),
        html.Div([
            html.Strong("Calculation Time: "),
            html.Span(f"Calculation #{current_calcs}", style={'color': '#666'})
        ], style=styles.CALCULATION_HEADER),
        html.Div([
            html.Strong("Time Range: "),
            f"{start_time:.1f}ms - {end_time:.1f}ms"
        ], style=styles.CALCULATION_SECTION),
        html.Div([
            html.Strong("Overall Average: "),
            html.Span(f"{overall_avg:.2f}", id={'type': 'overall-average', 'index': current_calcs - 1})
        ], style=styles.CALCULATION_SECTION),
        # Collapsible section for individual averages
        html.Div([
            # Toggle button with arrow
            html.Button([
                html.I(className="fas fa-chevron-right", style={'marginRight': '8px', 'transition': 'transform 0.3s'}),
                html.Strong("Individual Strip Averages")
            ],
            id={'type': 'toggle-strip-averages', 'index': current_calcs},
            style=styles.STRIP_TOGGLE_BUTTON),
            # Content (hidden by default)
            html.Div([
                html.Div(f"Strip {strip_num}: {avg:.2f}", 
                        style=styles.STRIP_AVERAGE_ITEM)
                for strip_num, avg in sorted(strip_averages)
            ],
            id={'type': 'strip-averages-content', 'index': current_calcs},
            style=styles.STRIP_AVERAGES_CONTENT)
        ])
    ], style=styles.CALCULATION_CONTAINER) 
"""
This module contains the fit graph component.
"""
from dash import html, dcc
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
from .fit_graph_style import *  # Import styles directly from the style file

def exponential_model(x, a, b):
    """Exponential decay model function."""
    return a * np.exp(-b * x)

def calc_mu(thicknesses, averages):
    """Calculate the exponential fit parameters."""
    if len(thicknesses) < 2:  # Need at least 2 points for a fit
        return None, None
    
    try:
        popt, pcov = curve_fit(exponential_model, thicknesses, averages, p0=(1, 1))
        return popt[0], popt[1]  # a, b parameters
    except:
        return None, None

def create_fit_graph(calculation_results):
    """Create the exponential fit graph component."""
    # Extract valid thickness-average pairs
    valid_pairs = [(r.thickness, r.overall_average) 
                  for r in calculation_results 
                  if r.thickness is not None]
    
    if len(valid_pairs) < 2:
        return html.Div(
            "No data points available for fitting", 
            style=NO_DATA_MESSAGE
        )

	# Extract thicknesses and averages
    thicknesses, averages = zip(*valid_pairs)
    thicknesses = np.array(thicknesses)
    averages = np.array(averages)
    
    # Calculate fit
    a, b = calc_mu(thicknesses, averages)
    if a is None or b is None:
        return html.Div(
            "Unable to calculate exponential fit", 
            style=NO_DATA_MESSAGE
        )
    
    # Generate points for the fit line
    x_fit = np.linspace(0, max(thicknesses), 100)
    y_fit = exponential_model(x_fit, a, b)
    
    # Create the figure
    fig = go.Figure()
    
    # Add experimental points
    fig.add_trace(go.Scatter(
        x=thicknesses,
        y=averages,
        mode='markers',
        name='Experimental',
        marker=EXPERIMENTAL_MARKER,
        hovertemplate="Thickness: %{x:.2f} cm<br>Response: %{y:.3f}<extra></extra>"
    ))
    
    # Add fit line
    fig.add_trace(go.Scatter(
        x=x_fit,
        y=y_fit,
        mode='lines',
        name='Exponential fit',
        line=FIT_LINE,
        hovertemplate="Thickness: %{x:.2f} cm<br>Response: %{y:.3f}<extra></extra>"
    ))
    
    # Update layout
    fig.update_layout(
        title=f'Exponential Fit (μ = {b:.3f} cm⁻¹)',
        xaxis_title='Thickness (cm)',
        yaxis_title='Response / Response step 0',
        showlegend=True,
        legend=LEGEND,
        margin=MARGIN,
        height=400
    )
    
    # Update axes to show 2 decimal places
    fig.update_xaxes(tickformat=".2f")
    fig.update_yaxes(tickformat=".3f")
    
    return html.Div([
        dcc.Graph(
            figure=fig,
            style=GRAPH
        )
    ], style=CONTAINER) 

from dash import html, dcc
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
from state import AppState
from .fit_graph_style import *

def exponential_model(x, a, b):
	"""Exponential decay model function."""
	return a * np.exp(-b * x)

def calc_mu(thicknesses, averages):
	"""Calculate the exponential fit parameters."""
	try:
		popt, pcov = curve_fit(exponential_model, thicknesses, averages, p0=(1, 1))
		return popt[0], popt[1]  # a, b parameters
	except:
		return None, None

def create_fit_graph(thicknesses, averages, x_fit, y_fit, mu):
	# Create the figure
	fig = go.Figure()
	
	# Add experimental points
	fig.add_trace(go.Scatter(
		x=thicknesses,
		y=averages,
		mode='markers',
		name='Experimental',
		marker=dict(color='orange', symbol='triangle-up', size=10),
		hovertemplate="Thickness: %{x:.2f} cm<br>Response: %{y:.3f}<extra></extra>"
	))
	
	# Add fit line
	fig.add_trace(go.Scatter(
		x=x_fit,
		y=y_fit,
		mode='lines',
		name='Exponential fit',
		line=dict(color='black', dash='dash'),
		hovertemplate="Thickness: %{x:.2f} cm<br>Response: %{y:.3f}<extra></extra>"
	))
	
	# Update layout
	fig.update_layout(
		title=dict(
			text=f'Exponential Fit (μ = {mu:.3f} cm⁻¹)',
			font=dict(weight='bold', color='#666', size=20)
		),
		xaxis=dict(title=dict(text='Thickness (cm)', font=dict(weight='bold', color='#666'))),
		yaxis=dict(title=dict(text='Response / Response step 0', font=dict(weight='bold', color='#666'))),
		showlegend=True,
		legend=dict(x=0.99, y=0.95, xanchor='right', yanchor='top'),
		height=400
	)
	
	# Update axes to show 2 decimal places
	fig.update_xaxes(tickformat=".2f")
	fig.update_yaxes(tickformat=".3f")

	return fig;

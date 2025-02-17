import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

def exponential_model(x, a, b):
	"""Exponential decay model function."""
	return a * np.exp(-b * x)

def calc_mu(x, y):
	"""Calculate the exponential fit parameters."""
	try:
		popt, pcov = curve_fit(exponential_model, x, y, p0=(1, 1))
		return popt[0], popt[1]
	except:
		return None, None

def exponential_fit_figure(x, y, x_fit, y_fit, mu):
	fig = go.Figure()
	
	fig.update_layout(
		title=dict(
			text=f'Exponential Fit (μ = {mu:.3f} cm⁻¹)',
			font=dict(weight='bold', color='#666', size=20)
		),
		xaxis=dict(title=dict(text='Thickness (cm)', font=dict(weight='bold', color='#666'))),
		yaxis=dict(title=dict(text='Response average (qdc)', font=dict(weight='bold', color='#666'))),
		showlegend=True,
		height=400,
		modebar_remove=['select2d', 'lasso2d']
	)
	
	# Update axes to show 2 decimal places for x and 0 decimal places for y
	fig.update_xaxes(tickformat=".2f")
	fig.update_yaxes(tickformat=".0f")
	
	# Add experimental points
	fig.add_trace(go.Scatter(
		x=x,
		y=y,
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

	return fig;

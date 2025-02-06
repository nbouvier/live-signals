"""
This module contains styles for the calculation result component.
"""

from styles import *

CONTAINER = {
	'display': 'flex',
	'justifyContent': 'space-between',
	'backgroundColor': 'rgba(188, 188, 188, 0.1)',
	'borderRadius': '6px',
	'border': '1px solid #ddd',
	'color': '#444'
}

HEADER = {
	'display': 'flex',
	'justifyContent': 'space-between',
	'alignItems': 'flex-start'
}

TIME_RANGE = {
	'color': '#666',
	'font-size': '12px'
}

THICKNESS_CONTAINER = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '2px'
}

THICKNESS_INPUT = {
	'width': '80px',
	'padding': f'{SPACING_UNIT} {SPACING_SMALL}',
	'border': '1px solid #ccc',
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL
}

INDIVIDUAL_AVERAGES_BUTTON = {
	'width': '100%',
	'textAlign': 'left',
	'padding': '8px',
	'backgroundColor': 'transparent',
	'border': 'none',
	'cursor': 'pointer',
	'display': 'flex',
	'alignItems': 'center',
	'gap': '8px'
}

TOGGLE_ICON = {
	'transition': 'transform 0.3s'
}

AVERAGES_CONTENT = {
	'display': 'none',
	'padding': '10px',
	'backgroundColor': '#f8f9fa',
	'borderRadius': '4px',
	'marginTop': '8px'
}

AVERAGE_ITEM = {
	'padding': '4px 0',
	'color': '#666',
	'fontSize': '14px'
} 

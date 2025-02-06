"""
This module contains styles for the averages panel component.
"""

from styles import *

CALCULATE_BUTTON = {
	'display': 'flex',
	'justifyContent': 'center',
	'backgroundColor': PRIMARY_COLOR,
	'color': 'white',
	'padding': f'{SPACING_SMALL} {SPACING_MEDIUM}',
	'border': 'none',
	'borderRadius': BORDER_RADIUS,
	'cursor': 'pointer',
	'fontSize': FONT_SIZE_LARGE,
	'transition': 'background-color 0.3s',
	'width': '100%',
	'marginBottom': '10px'
}

AVERAGES_CONTENT = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '10px'
}

BUTTON_ICON = {
	'marginRight': SPACING_SMALL
} 

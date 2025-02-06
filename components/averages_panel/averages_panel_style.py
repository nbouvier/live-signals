"""
This module contains styles for the averages panel component.
"""

from styles import (
	PRIMARY_COLOR,
	SPACING_MEDIUM,
	SPACING_SMALL,
	SPACING_LARGE,
	FONT_SIZE_NORMAL,
	BORDER_RADIUS
)

CALCULATE_BUTTON = {
	'display': 'flex',
	'justifyContent': 'center',
	'backgroundColor': PRIMARY_COLOR,
	'color': 'white',
	'padding': '10px 20px',
	'border': 'none',
	'borderRadius': '4px',
	'cursor': 'pointer',
	'fontSize': '16px',
	'transition': 'background-color 0.3s',
	'width': '100%',
	'marginBottom': '10px'
}

AVERAGES_CONTENT = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '10px',
	'maxHeight': 'calc(100vh - 200px)',
	'overflowY': 'auto'
}

BUTTON_ICON = {
	'marginRight': SPACING_SMALL
} 

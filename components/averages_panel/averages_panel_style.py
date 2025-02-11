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

STRIP_AVERAGES_CONTENT = {
	'display': 'none',
	'padding': '10px',
	'backgroundColor': '#f8f9fa',
	'borderRadius': '4px',
	'marginTop': '8px'
}

STRIP_AVERAGE_ITEM = {
	'padding': '4px 0',
	'color': '#666',
	'fontSize': '14px'
}

BUTTON_CONTAINER = {
	'display': 'flex',
	'flexDirection': 'column'
}

SELECT_BUTTON = {
	'border': '1px solid #888',
	'borderTopRightRadius': '4px',
	'borderBottomWidth': '0px',
	'backgroundColor': 'transparent',
	'color': '#666',
	'width': '32px',
	'padding': '4px',
	'cursor': 'pointer'
}

DELETE_BUTTON = {
	'flex': 1,
	'border': '1px solid #dc3545',
	'borderBottomRightRadius': '4px',
	'backgroundColor': 'transparent',
	'color': '#dc3545',
	'width': '32px',
	'padding': '4px',
	'cursor': 'pointer'
}

NO_AVERAGE = {
	'color': MUTED_TEXT_COLOR
}

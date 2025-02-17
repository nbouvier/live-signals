"""
This module contains styles for the averages panel component.
"""

from styles import *

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

COLOR_BOX = {
	'width': '12px',
	'height': '12px',
	'marginTop': '-2px',
	'marginRight': '10px',
	'display': 'inline-block',
	'verticalAlign': 'middle',
	'borderRadius': '2px'
}

TIME_RANGE = {
	'color': '#666',
	'font-size': '12px'
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
	'borderRadius': 0,
	'borderBottom': 'none',
	'borderTopRightRadius': '4px',
	'width': '32px',
	'padding': '4px'
}

DELETE_BUTTON = {
	'flex': 1,
	'borderRadius': 0,
	'borderBottomRightRadius': '4px',
	'width': '32px',
	'padding': '4px'
}

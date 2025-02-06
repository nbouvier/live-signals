"""
This module contains styles for the file selector component.
"""

from styles import *

ADD_FILE_BUTTON = {
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

BUTTON_ICON = {
	'marginRight': SPACING_SMALL
} 

FILES_LIST = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '10px'
}

FILE_CARD = {
	'display': 'flex',
	'backgroundColor': 'rgba(188, 188, 188, 0.1)',
	'borderRadius': '6px',
	'border': '1px solid #ddd',
	'color': '#444',
}

FILE_CARD_BODY = {
	'display': 'flex',
	'flex': 1,
	'alignItems': 'center',
	'padding': '8px 12px'
}

FILE_NAME_CONTAINER = {
	'fontSize': '12px',
	'color': MUTED_TEXT_COLOR
}

FILE_NAME = {
	'marginLeft': '6px',
	'fontWeight': 'bold'
}

OFFSET_INPUT = {
	'marginLeft': SPACING_SMALL,
	'width': '60px',
	'padding': f'{SPACING_UNIT} {SPACING_SMALL}',
	'border': '1px solid #ccc',
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL
}

FILE_DELETE = {
	'alignSelf': 'stretch',
	'border': '1px solid #dc3545',
	'borderTopRightRadius': '4px',
	'borderBottomRightRadius': '4px',
	'backgroundColor': 'transparent',
	'color': '#dc3545',
	'width': '32px',
	'padding': '4px',
	'cursor': 'pointer',
	'transition': 'all 0.3s'
}

NO_FILE = {
	'color': MUTED_TEXT_COLOR
}

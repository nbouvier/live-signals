"""
This module contains styles for the strip selector component.
"""

from styles import *

STRIP_SELECTOR = {
	'width': '100%',
	'maxHeight': 'calc(100vh - 190px)',
	'padding': SPACING_MEDIUM,
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'backgroundColor': BACKGROUND_COLOR,
	'margin': f'{SPACING_MEDIUM} 0'
}

BUTTON = {
	'backgroundColor': SECONDARY_COLOR,
	'color': 'white',
	'border': 'none',
	'borderRadius': BORDER_RADIUS,
	'cursor': 'pointer',
	'fontSize': FONT_SIZE_SMALL
}

SELECT_ALL_BUTTON = {
	**BUTTON,
	'backgroundColor': 'green'
}

UNSELECT_ALL_BUTTON = {
	**BUTTON,
	'backgroundColor': WARNING_COLOR
}

SELECT_BUTTON = {
	**BUTTON,
	'backgroundColor': PRIMARY_COLOR
}

BUTTON_CONTAINER = {
	'display': 'flex',
	'gap': SPACING_SMALL,
	'marginBottom': SPACING_SMALL
}

OVERLAY = {
	'position': 'fixed',
	'top': '0',
	'left': '-400px',
	'height': '100vh',
	'width': '400px',
	'backgroundColor': 'white',
	'boxShadow': SHADOW_MEDIUM,
	'transition': f'left {TRANSITION_NORMAL} ease-in-out',
	'zIndex': Z_INDEX_OVERLAY,
	'padding': f'{SPACING_MEDIUM} {SPACING_MEDIUM} 60px {SPACING_MEDIUM}',
	'overflow': 'hidden'
}

OVERLAY_VISIBLE = {
	**OVERLAY,
	'left': '0'
}

TOGGLE_BUTTON = {
	'position': 'fixed',
	'top': SPACING_MEDIUM,
	'left': SPACING_MEDIUM,
	'zIndex': Z_INDEX_OVERLAY + 1,
	'backgroundColor': PRIMARY_COLOR,
	'color': 'white',
	'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
	'border': 'none',
	'borderRadius': BORDER_RADIUS,
	'cursor': 'pointer',
	'fontSize': FONT_SIZE_NORMAL,
	'boxShadow': SHADOW_MEDIUM
}

STRIP_LABEL = {
	'display': 'block',
	'padding': SPACING_SMALL,
	'backgroundColor': 'white',
	'borderRadius': BORDER_RADIUS,
	'margin': SPACING_SMALL,
	'cursor': 'pointer',
	'transition': f'background-color {TRANSITION_NORMAL}',
	':hover': {'backgroundColor': '#e6e6e6'}
}

DROPDOWN_STYLE = {
	'width': '100%',
	'backgroundColor': 'white',
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL
}

SELECTED_STRIPS_CONTAINER = {
	'display': 'flex',
	'flexWrap': 'wrap',
	'gap': SPACING_SMALL,
	'paddingLeft': SPACING_UNIT,
	'overflowY': 'auto',
	'height': '110px',
	'marginBottom': SPACING_MEDIUM
}

SELECTED_STRIP_TAG = {
	'display': 'flex',
	'justifyContent': 'center',
	'backgroundColor': 'rgba(51, 51, 51, 0.1)',
	'borderRadius': BORDER_RADIUS,
	'padding': f'{SPACING_UNIT} {SPACING_SMALL}',
	'display': 'flex',
	'alignItems': 'center',
	'gap': SPACING_SMALL,
	'fontSize': FONT_SIZE_NORMAL,
	'color': '#666',
	'fontWeight': 'bold',
	'fontSize': FONT_SIZE_NORMAL,
	'cursor': 'pointer',
	'width': '30px',
}

CUSTOM_DROPDOWN_CONTAINER = {
	'position': 'relative',
	'width': '100%',
	'marginBottom': SPACING_MEDIUM
}

CUSTOM_DROPDOWN_INPUT_CONTAINER = {
	'width': '100%',
	'position': 'relative',
	'cursor': 'pointer',
	'zIndex': Z_INDEX_OVERLAY
}

CUSTOM_DROPDOWN_INPUT = {
	'width': '100%',
	'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
	'paddingRight': '30px',  # Space for the arrow
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL,
	'backgroundColor': 'white',
	'cursor': 'pointer',
	'outline': 'none',
	'boxSizing': 'border-box'
}


DROPDOWN_ARROW = {
	'position': 'absolute',
	'right': SPACING_MEDIUM,
	'top': '50%',
	'transform': 'translateY(-50%)',
	'pointerEvents': 'none',
	'color': '#666'
}

CUSTOM_DROPDOWN_LIST = {
	'position': 'absolute',
	'top': 'calc(100% + 4px)',
	'left': '0',
	'right': '0',
	'maxHeight': '300px',
	'overflowY': 'auto',
	'backgroundColor': 'white',
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'boxShadow': SHADOW_MEDIUM,
	'display': 'block',
	'zIndex': Z_INDEX_OVERLAY
}

CUSTOM_DROPDOWN_ITEM = {
	'padding': SPACING_MEDIUM,
	'cursor': 'pointer',
	'transition': f'background-color {TRANSITION_NORMAL}',
	'backgroundColor': 'white',
	'hover': {
		'backgroundColor': f'{PRIMARY_COLOR}11'
	}
}

STRIP_DROPDOWN_BACKGROUND = {
	'height': '100vh',
	'width': '100vw',
	'position': 'fixed',
	'top': 0,
	'left': 0,
	'zIndex': f'calc({Z_INDEX_OVERLAY} - 1)'
}

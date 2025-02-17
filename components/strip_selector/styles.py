from styles import *

BUTTON_CONTAINER = {
	'display': 'flex',
	'gap': SPACING_SMALL,
	'justifyContent': 'space-between',
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
	'maxHeight': '110px'
}

STRIP_TAG = {
	'backgroundColor': 'rgba(188, 188, 188, 0.1)',
	'border': '1px solid #ddd',
	'padding': f'6px {SPACING_SMALL} {SPACING_UNIT} {SPACING_SMALL}',
	'color': '#666',
	'fontWeight': 'bold',
	'width': '30px'
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
	'cursor': 'text',
	'outline': 'none',
	'boxSizing': 'border-box'
}

DROPDOWN_ARROW = {
	'position': 'absolute',
	'right': SPACING_LARGE,
	'top': '50%',
	'transform': 'translateY(-50%)',
	'pointerEvents': 'none',
	'color': '#666'
}

CUSTOM_DROPDOWN_LIST = {
	'display': 'flex',
	'flexWrap': 'wrap',
	'gap': SPACING_SMALL,
	'padding': SPACING_UNIT,
	'position': 'absolute',
	'top': 'calc(100% + 4px)',
	'left': '0',
	'right': '0',
	'maxHeight': '150px',
	'overflowY': 'auto',
	'backgroundColor': 'white',
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'boxShadow': SHADOW_MEDIUM,
	'zIndex': Z_INDEX_OVERLAY
}

STRIP_DROPDOWN_BACKGROUND = {
	'height': '100vh',
	'width': '100vw',
	'position': 'fixed',
	'top': 0,
	'left': 0,
	'zIndex': f'calc({Z_INDEX_OVERLAY} - 1)'
}

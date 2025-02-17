from styles import *

BASE_POPUP = {
	'display': 'block',
	'position': 'fixed',
	'bottom': SPACING_MEDIUM,
	'right': SPACING_MEDIUM,
	'backgroundColor': 'white',
	'padding': SPACING_MEDIUM,
	'borderRadius': BORDER_RADIUS,
	'boxShadow': SHADOW_MEDIUM,
	'zIndex': Z_INDEX_POPUP,
	'textAlign': 'center',
	'transition': f'transform {TRANSITION_NORMAL} ease-out',
	'transform': 'translateY(0)',
	'border': f'2px solid {DANGER_COLOR}'
}

HIDDEN_POPUP = {
	**BASE_POPUP,
	'transform': 'translateY(100%)'
}

ERROR_MESSAGE = {
	'color': DANGER_COLOR,
	'fontWeight': 'bold'
}

CLOSE_BUTTON = {
	'backgroundColor': DANGER_COLOR,
	'color': 'white',
	'border': 'none',
	'padding': '8px 16px',
	'borderRadius': BORDER_RADIUS,
	'cursor': 'pointer',
	'display': 'block'
} 

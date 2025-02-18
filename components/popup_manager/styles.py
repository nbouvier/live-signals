from styles import *

POPUP_LIST = {
	'display': 'flex',
	'flexDirection': 'column-reverse',
	'gap': SPACING_SMALL,
	'position': 'fixed',
	'bottom': SPACING_MEDIUM,
	'right': SPACING_MEDIUM,
	'zIndex': Z_INDEX_POPUP
}

POPUP = {
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'space-between',
	'gap': SPACING_SMALL,
	'backgroundColor': 'rgba(255, 0, 0, 0.1)',
	'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
	'borderRadius': BORDER_RADIUS,
	'boxShadow': SHADOW_MEDIUM,
	'color': 'rgb(220, 53, 69)',
	'maxWidth': '300px'
}

POPUP_ICON = {
	'display': 'flex',
	'alignSelf': 'start',
	'cursor': 'pointer'
} 

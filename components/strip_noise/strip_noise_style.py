from styles import *

STRIP_LIST_TOGGLE = {
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'space-between',
	'cursor': 'pointer',
	'color': MUTED_TEXT_COLOR,
	'fontSize': FONT_SIZE_LARGE
}

STRIP_LIST = {
	'display': 'flex',
	'flexWrap': 'wrap',
	'gap': SPACING_SMALL,
	'maxHeight': '150px',
	'overflowY': 'auto'
}

STRIP = {
	'display': 'flex',
	'gap': SPACING_UNIT
}

STRIP_LABEL = {
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'center',
	'width': '20px',
	'color': MUTED_TEXT_COLOR,
	'fontSize': FONT_SIZE_SMALL,
	'fontWeight': 'bold'
}

STRIP_NOISE = {
	**INPUT,
	'fontSize': FONT_SIZE_TINY,
	'width': '40px'
}

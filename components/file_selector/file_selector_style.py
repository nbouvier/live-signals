from styles import *

FILE = {
	'display': 'flex',
	'flexDirection': 'column',
	'color': '#444'
}

FILE_BODY = {
	'display': 'flex',
	'flexDirection': 'column',
	'flex': 1,
	'gap': SPACING_LARGE,
	'alignItems': 'center',
	'padding': f'{SPACING_SMALL} {SPACING_ZERO} {SPACING_XLARGE} {SPACING_ZERO}'
}

FILE_HEADER = {
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'space-between',
	'fontSize': FONT_SIZE_SMALL,
	'fontWeight': 'bold',
	'color': MUTED_TEXT_COLOR,
	'cursor': 'pointer',
	'padding': f'{SPACING_SMALL} {SPACING_ZERO}'
}

FILE_NAME = {
	'marginLeft': '6px'
}

OFFSET_INPUT = {
	'marginLeft': SPACING_SMALL,
	'width': '60px',
	'padding': f'{SPACING_UNIT} {SPACING_SMALL}',
	'border': '1px solid #ccc',
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL
}

FILE_GRAPHS_CONTAINER = {
	'width': '820px',
	'minWidth': '820px'
}

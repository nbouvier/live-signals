# Color palette
PRIMARY_COLOR = '#007bff'
SECONDARY_COLOR = '#6c757d'
DANGER_COLOR = '#ff3333'
WARNING_COLOR = '#dc3545'
BACKGROUND_COLOR = '#f8f9fa'
TEXT_COLOR = '#333'
MUTED_TEXT_COLOR = '#6c757d'

# Border styles
BORDER_RADIUS = '4px'
BORDER_COLOR = '#ddd'
BORDER_STYLE = '1px solid #dee2e6'

# Spacing
SPACING_ZERO = '0px'
SPACING_TINY = '2px'
SPACING_UNIT = '4px'
SPACING_SMALL = '8px'
SPACING_NORMAL = '12px'
SPACING_MEDIUM = '16px'
SPACING_LARGE = '24px'
SPACING_XLARGE = '32px'

# Font sizes
FONT_SIZE_TINY = '10px'
FONT_SIZE_SMALL = '12px'
FONT_SIZE_NORMAL = '14px'
FONT_SIZE_LARGE = '16px'

# Z-index layers
Z_INDEX_OVERLAY = 1000
Z_INDEX_POPUP = 1001
Z_INDEX_TOOLTIP = 1002

# Transitions
TRANSITION_FAST = '0.2s'
TRANSITION_NORMAL = '0.3s'
TRANSITION_SLOW = '0.5s'

# Common styles
SHADOW_LIGHT = '0 2px 4px rgba(0,0,0,0.1)'
SHADOW_MEDIUM = '0 2px 4px rgba(0, 0, 0, 0.1)'
SHADOW_HEAVY = '0 4px 16px rgba(0,0,0,0.2)'

# Layout styles
MAIN_CONTAINER = {
	'display': 'flex',
	'boxSizing': 'border-box',
	'minHeight': '100vh',
	'margin': 0,
	'padding': 0,
	'background-color': 'white'
}

SIDE_PANEL = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '24px',
	'width': '351px',
	'minWidth': '351px',
	'backgroundColor': BACKGROUND_COLOR,
	'padding': SPACING_MEDIUM,
	'border': '1px solid #ddd',
	'boxSizing': 'border-box'
}

TOGGLE_SIDE_PANEL_CONTAINER= {
	'display': 'flex',
	'width': '10px',
	'position': 'relative'
}

TOGGLE_SIDE_PANEL = {
	'opacity': '0',
	'display': 'flex',
	'alignItems': 'center',
	'position': 'absolute',
	'top': '15px',
	'left': '-1px',
	'width': '35px',
	'height': '50px',
	'paddingLeft': SPACING_SMALL,
	'backgroundColor': BACKGROUND_COLOR,
	'border': '1px solid #ddd',
	'borderLeft': 'none',
	'borderTopRightRadius': '25px',
	'borderBottomRightRadius': '25px',
	'color': PRIMARY_COLOR,
	'zIndex': 1,
	'cursor': 'pointer',
	'transition': 'all 0.3s ease-in-out'
}

CENTER_PANEL = {
	'display': 'flex',
	'flexDirection': 'column',
	'flex': '1',
	'gap': SPACING_MEDIUM,
	'padding': SPACING_MEDIUM,
	'paddingLeft': '6px',
	'boxSizing': 'border-box',
	'overflowY': 'auto'
}

# Overlay styles
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

# Click catcher style
CLICK_CATCHER = {
	'position': 'fixed',
	'top': '0',
	'left': '0',
	'width': '100vw',
	'height': '100vh',
	'backgroundColor': 'rgba(0, 0, 0, 0.5)',
	'zIndex': Z_INDEX_OVERLAY - 1
}

# Selection indicator styles
SELECTION_INDICATOR = {
	'width': '20px',
	'height': '20px',
	'borderRadius': '50%',
	'display': 'inline-block',
	'marginRight': '10px'
} 

# Layout styles
MAIN_CONTENT = {
	'marginLeft': '60px',  # Space for toggle button
	'marginRight': '20px',
	'width': 'calc(100% - 80px)',  # Account for margins
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '20px'
} 

# Hidden style
HIDDEN = {
	'display': 'none'
}

INPUT_CONTAINER = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '2px'
}

INPUT_LABEL = {
	'fontSize': '10px',
	'fontWeight': 'bold',
	'color': '#666'
}

INPUT = {
	'width': '80px',
	'padding': f'{SPACING_UNIT} {SPACING_SMALL}',
	'border': '1px solid #ccc',
	'borderRadius': BORDER_RADIUS,
	'fontSize': FONT_SIZE_NORMAL
}

GRAPHS_CONTAINER = {
	'overflowX': 'auto'
}

GRAPH_CONTAINER = {
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'center',
	'height': '400px',
	'minHeight': '400px',
	'padding': '20px 60px 20px 60px',
	'backgroundColor': BACKGROUND_COLOR,
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'color': MUTED_TEXT_COLOR,
	'fontSize': FONT_SIZE_LARGE
}

GRAPH = {
	'display': 'block'
}

GRAPH_PLACEHOLDER = {
	'display': 'flex',
	'justifyContent': 'center',
	'alignItems': 'center'
}

TAB_GRAPH_CONTAINER = {
	**GRAPH_CONTAINER,
	'borderTop': 'none',
	'borderRadius': 'none',
	'borderBottomLeftRadius': BORDER_RADIUS,
	'borderBottomRightRadius': BORDER_RADIUS
}

TAB = {
	'color': MUTED_TEXT_COLOR,
	'fontSize': FONT_SIZE_SMALL,
	'backgroundColor': 'white',
	'padding': '10px',
	'borderTopLeftRadius': BORDER_RADIUS,
	'borderTopRightRadius': BORDER_RADIUS
}

SELECTED_TAB = {
	'color': MUTED_TEXT_COLOR,
	'fontSize': FONT_SIZE_SMALL,
	'fontWeight': 'bold',
	'backgroundColor': BACKGROUND_COLOR,
	'padding': '10px',
	'borderTopLeftRadius': BORDER_RADIUS,
	'borderTopRightRadius': BORDER_RADIUS
}

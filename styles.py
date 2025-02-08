"""
This module contains global style variables used across the application.
"""

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
SPACING_UNIT = '4px'
SPACING_SMALL = '8px'
SPACING_MEDIUM = '16px'
SPACING_LARGE = '24px'

# Font sizes
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
	'width': '100vw',
	'margin': 0,
	'padding': 0,
	'background-color': 'white'
}

SIDE_PANEL = {
	'display': 'flex',
	'flexDirection': 'column',
	'gap': '24px',
	'width': '335px',
	'minWidth': '335px',
	'backgroundColor': BACKGROUND_COLOR,
	'padding': SPACING_MEDIUM,
	'border': '1px solid #ddd',
	'zIndex': 1,
	'boxSizing': 'border-box'
}

CENTER_PANEL = {
	'display': 'flex',
	'flexDirection': 'column',
	'flex': '1',
	'gap': SPACING_MEDIUM,
	'padding': SPACING_MEDIUM,
	'boxSizing': 'border-box',
	'overflowY': 'scroll'
}

# Strip selector styles
STRIP_SELECTOR = {
	'display': 'grid',
	'gridTemplateColumns': 'repeat(auto-fill, minmax(80px, 1fr))',
	'gap': '5px',
	'overflowY': 'auto',
	'padding': '10px 0',
	'backgroundColor': BACKGROUND_COLOR
}

# Button styles
BUTTON = {
	'backgroundColor': '#4CAF50',
	'color': 'white',
	'padding': '10px 20px',
	'border': 'none',
	'borderRadius': '4px',
	'margin': '5px',
	'cursor': 'pointer',
	'fontSize': '14px'
}

BUTTON_CONTAINER = {
	'display': 'flex',
	'gap': '10px',
	'marginBottom': '10px'
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

# Popup styles
BASE_POPUP = {
	'position': 'fixed',
	'top': '20px',
	'left': '50%',
	'transform': 'translateX(-50%)',
	'backgroundColor': 'white',
	'padding': SPACING_MEDIUM,
	'borderRadius': BORDER_RADIUS,
	'boxShadow': SHADOW_MEDIUM,
	'zIndex': Z_INDEX_OVERLAY + 1,
	'display': 'flex',
	'alignItems': 'center',
	'gap': SPACING_MEDIUM
}

HIDDEN_POPUP = {
	**BASE_POPUP,
	'display': 'none'
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

# Close button style
CLOSE_BUTTON = {
	'backgroundColor': 'transparent',
	'border': 'none',
	'color': MUTED_TEXT_COLOR,
	'cursor': 'pointer',
	'padding': '4px',
	'display': 'flex',
	'alignItems': 'center',
	'justifyContent': 'center',
	'transition': f'color {TRANSITION_NORMAL}',
	':hover': {
		'color': WARNING_COLOR
	}
}

# Error message style
ERROR_MESSAGE = {
	'color': '#ff3333',
	'fontWeight': 'bold'
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

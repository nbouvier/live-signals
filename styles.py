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
	'height': '100vh',
	'width': '100vw',
	'margin': 0,
	'padding': 0,
	'background-color': 'white'
}

SIDE_PANEL = {
	'width': '300px',
	'minWidth': '300px',
	'backgroundColor': BACKGROUND_COLOR,
	'borderRadius': BORDER_RADIUS,
	'padding': SPACING_MEDIUM,
	'position': 'fixed',
	'top': 0,
	'height': '100vh',
	'overflowY': 'auto',
	'zIndex': 1
}


LEFT_PANEL = {
	**SIDE_PANEL,
	'left': 0
}

RIGHT_PANEL = {
	**SIDE_PANEL,
	'right': 0
}

CENTER_PANEL = {
	'flex': '1',
	'display': 'flex',
	'flexDirection': 'column',
	'gap': SPACING_MEDIUM,
	'minWidth': '0',  # Prevents flex items from overflowing
	'marginLeft': '300px',  # Width of left panel
	'marginRight': '300px',  # Width of right panel
	'padding': SPACING_MEDIUM
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

# Toggle button
TOGGLE_BUTTON = {
	'position': 'fixed',
	'top': SPACING_MEDIUM,
	'left': SPACING_MEDIUM,
	'zIndex': Z_INDEX_OVERLAY - 2,
	'backgroundColor': PRIMARY_COLOR,
	'color': 'white',
	'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
	'border': 'none',
	'borderRadius': BORDER_RADIUS,
	'cursor': 'pointer',
	'fontSize': FONT_SIZE_NORMAL,
	'boxShadow': SHADOW_MEDIUM,
	'display': 'flex',
	'alignItems': 'center'
}

# Base graph styles
BASE_GRAPH = {
	'height': '800px',
	'width': '100%'
}

BASE_PLACEHOLDER = {
	'height': '800px',
	'width': '100%',
	'backgroundColor': '#f9f9f9',
	'border': '1px solid #ddd',
	'borderRadius': '5px',
	'display': 'flex',
	'justifyContent': 'center',
	'alignItems': 'center',
	'color': '#666',
	'fontSize': '18px'
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


FILE_CARD = {
	'padding': '8px 12px',
	'backgroundColor': 'white',
	'borderRadius': BORDER_RADIUS,
	'border': BORDER_STYLE,
	'fontSize': '14px',
	'display': 'flex',
	'alignItems': 'center',
	'gap': '8px',
	'position': 'relative',
	'paddingRight': '100px'  # Space for time offset input
}

TIME_OFFSET_INPUT = {
	'width': '80px',
	'padding': '4px 8px',
	'border': BORDER_STYLE,
	'borderRadius': BORDER_RADIUS,
	'position': 'absolute',
	'right': '8px',
	'top': '50%',
	'transform': 'translateY(-50%)'
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

"""
This module contains global style variables used across the application.
"""

# Color palette
PRIMARY_COLOR = '#2196F3'
SECONDARY_COLOR = '#4CAF50'
DANGER_COLOR = '#ff3333'
WARNING_COLOR = '#f44336'
BACKGROUND_COLOR = '#f9f9f9'
TEXT_COLOR = '#333'
MUTED_TEXT_COLOR = '#666'

# Border styles
BORDER_RADIUS = '4px'
BORDER_COLOR = '#ddd'
BORDER_STYLE = f'1px solid {BORDER_COLOR}'

# Spacing
SPACING_UNIT = '4px'
SPACING_SMALL = '8px'
SPACING_MEDIUM = '16px'
SPACING_LARGE = '24px'

# Font sizes
FONT_SIZE_SMALL = '12px'
FONT_SIZE_NORMAL = '14px'
FONT_SIZE_LARGE = '18px'

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
SHADOW_MEDIUM = '0 2px 10px rgba(0,0,0,0.1)'
SHADOW_HEAVY = '0 4px 16px rgba(0,0,0,0.2)'

# Strip selector styles
STRIP_SELECTOR = {
    'display': 'grid',
    'gridTemplateColumns': 'repeat(auto-fill, minmax(100px, 1fr))',
    'gap': '5px',
    'maxHeight': 'calc(100vh - 190px)',
    'overflowY': 'auto',
    'padding': '10px',
    'border': '1px solid #ddd',
    'borderRadius': '5px',
    'backgroundColor': '#f9f9f9',
    'margin': '10px 0'
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
    'boxShadow': '2px 0 10px rgba(0,0,0,0.1)',
    'transition': 'left 0.3s ease-in-out',
    'zIndex': '1000',
    'padding': '20px 20px 60px 20px',
    'overflow': 'hidden'
}

OVERLAY_VISIBLE = {
    'position': 'fixed',
    'top': '0',
    'left': '0',
    'height': '100vh',
    'width': '400px',
    'backgroundColor': 'white',
    'boxShadow': '2px 0 10px rgba(0,0,0,0.1)',
    'transition': 'left 0.3s ease-in-out',
    'zIndex': '1000',
    'padding': '20px 20px 60px 20px',
    'overflow': 'hidden'
}

TOGGLE_BUTTON = {
    'position': 'fixed',
    'top': '20px',
    'left': '20px',
    'zIndex': '1001',
    'backgroundColor': '#2196F3',
    'color': 'white',
    'padding': '10px 20px',
    'border': 'none',
    'borderRadius': '4px',
    'cursor': 'pointer',
    'fontSize': '14px',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.2)'
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
    'display': 'block',
    'position': 'fixed',
    'bottom': '20px',
    'right': '20px',
    'backgroundColor': 'white',
    'padding': '20px',
    'borderRadius': '5px',
    'boxShadow': '0 2px 10px rgba(0,0,0,0.1)',
    'zIndex': 1000,
    'textAlign': 'center',
    'transition': 'transform 0.3s ease-out',
    'transform': 'translateY(0)',
    'border': '2px solid #ff3333'
}

HIDDEN_POPUP = {
    **BASE_POPUP,
    'transform': 'translateY(100%)'
}

# Click catcher style
CLICK_CATCHER = {
    'display': 'block',
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'width': '100%',
    'height': '100%',
    'backgroundColor': 'rgba(0,0,0,0.3)',
    'zIndex': 999
}

# Close button style
CLOSE_BUTTON = {
    'backgroundColor': '#ff3333',
    'color': 'white',
    'border': 'none',
    'padding': '8px 16px',
    'borderRadius': '4px',
    'cursor': 'pointer',
    'display': 'block'
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
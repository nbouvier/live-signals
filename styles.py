"""
This module contains all the styles used in the application.
"""

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

# Graph styles
GRAPH_CONTAINER = {
    'position': 'relative',
    'height': '800px',
    'width': '100%',
    'backgroundColor': '#f9f9f9',
    'border': '1px solid #ddd',
    'borderRadius': '5px',
}

PLACEHOLDER = {
    'textAlign': 'center',
    'color': '#666',
    'fontSize': '18px'
}

LOADING = {
    'position': 'absolute',
    'top': '0',
    'left': '0',
    'width': '100%',
    'height': '100%',
    'backgroundColor': 'rgba(255, 255, 255, 0.7)',
    'zIndex': '100',
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center'
}

# Container styles
AVERAGES_CONTAINER = {
    'padding': '20px',
    'backgroundColor': 'white',
    'border': '1px solid #ddd',
    'borderRadius': '5px',
    'margin': '20px 0',
}

FLEX_CONTAINER = {
    'display': 'block',
    '@media (min-width: 992px)': {
        'display': 'flex',
        'gap': '20px',
        'alignItems': 'flex-start'
    }
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

# Calculation result styles
CALCULATION_CONTAINER = {
    'backgroundColor': '#f8f9fa',
    'padding': '15px',
    'borderRadius': '5px',
    'marginBottom': '15px'
}

CALCULATION_HEADER = {
    'marginBottom': '10px'
}

CALCULATION_SECTION = {
    'marginBottom': '10px'
}

# Strip averages toggle styles
STRIP_TOGGLE_BUTTON = {
    'backgroundColor': 'transparent',
    'border': 'none',
    'padding': '8px 0',
    'cursor': 'pointer',
    'display': 'flex',
    'alignItems': 'center',
    'width': '100%',
    'color': '#333',
    'marginBottom': '8px'
}

STRIP_AVERAGES_CONTENT = {
    'maxHeight': '300px',
    'overflowY': 'auto',
    'display': 'none',
    'padding': '10px',
    'backgroundColor': '#fff',
    'borderRadius': '4px',
    'border': '1px solid #eee'
}

STRIP_AVERAGE_ITEM = {
    'marginBottom': '4px'
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
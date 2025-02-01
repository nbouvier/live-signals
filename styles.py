"""
This module contains all the styles used in the application.
"""

# Strip selector styles
STRIP_SELECTOR_STYLE = {
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
BUTTON_STYLE = {
    'backgroundColor': '#4CAF50',
    'color': 'white',
    'padding': '10px 20px',
    'border': 'none',
    'borderRadius': '4px',
    'margin': '5px',
    'cursor': 'pointer',
    'fontSize': '14px'
}

BUTTON_CONTAINER_STYLE = {
    'display': 'flex',
    'gap': '10px',
    'marginBottom': '10px'
}

# Overlay styles
OVERLAY_STYLE = {
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

OVERLAY_VISIBLE_STYLE = {
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

TOGGLE_BUTTON_STYLE = {
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
GRAPH_CONTAINER_STYLE = {
    'position': 'relative',
    'height': '800px',
    'width': '100%',
    'backgroundColor': '#f9f9f9',
    'border': '1px solid #ddd',
    'borderRadius': '5px',
}

PLACEHOLDER_STYLE = {
    'textAlign': 'center',
    'color': '#666',
    'fontSize': '18px'
}

LOADING_STYLE = {
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
AVERAGES_CONTAINER_STYLE = {
    'padding': '20px',
    'backgroundColor': 'white',
    'border': '1px solid #ddd',
    'borderRadius': '5px',
    'margin': '20px 0',
}

FLEX_CONTAINER_STYLE = {
    'display': 'block',
    '@media (min-width: 992px)': {
        'display': 'flex',
        'gap': '20px',
        'alignItems': 'flex-start'
    }
} 
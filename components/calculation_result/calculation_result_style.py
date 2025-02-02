"""
This module contains styles for the calculation result component.
"""

CONTAINER = {
    'backgroundColor': 'white',
    'borderRadius': '8px',
    'padding': '15px',
    'marginBottom': '15px',
    'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'transition': 'box-shadow 0.3s',
    ':hover': {
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.15)'
    }
}

HEADER = {
    'display': 'flex',
    'justifyContent': 'space-between',
    'alignItems': 'flex-start'
}

TIME_RANGE = {
    'display': 'flex',
    'alignItems': 'center',
	'marginTop': '-8px',
    'marginBottom': '15px'
}

SECTION = {
    'marginBottom': '15px',
    'display': 'flex',
    'alignItems': 'center',
    'gap': '8px'
}

THICKNESS_INPUT = {
    'width': '80px',
    'padding': '4px 8px',
    'border': '1px solid #ccc',
    'borderRadius': '4px',
    'fontSize': '14px'
}

UNIT_LABEL = {
    'color': '#666',
    'fontSize': '14px'
}

TOGGLE_BUTTON = {
    'width': '100%',
    'textAlign': 'left',
    'padding': '8px',
    'backgroundColor': 'transparent',
    'border': 'none',
    'cursor': 'pointer',
    'display': 'flex',
    'alignItems': 'center',
    'gap': '8px'
}

TOGGLE_ICON = {
    'transition': 'transform 0.3s'
}

AVERAGES_CONTENT = {
    'display': 'none',
    'padding': '10px',
    'backgroundColor': '#f8f9fa',
    'borderRadius': '4px',
    'marginTop': '8px'
}

AVERAGE_ITEM = {
    'padding': '4px 0',
    'color': '#666',
    'fontSize': '14px'
} 

"""
This module contains styles for the graph display component.
"""

from styles import (
    BACKGROUND_COLOR,
    BORDER_STYLE,
    BORDER_RADIUS,
    MUTED_TEXT_COLOR,
    FONT_SIZE_LARGE,
    PRIMARY_COLOR
)

BASE_GRAPH = {
    'height': '800px',
    'width': '100%'
}

BASE_PLACEHOLDER = {
    'height': '800px',
    'width': '100%',
    'backgroundColor': BACKGROUND_COLOR,
    'border': BORDER_STYLE,
    'borderRadius': BORDER_RADIUS,
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center',
    'color': MUTED_TEXT_COLOR,
    'fontSize': FONT_SIZE_LARGE
}

CONTAINER = {
    'flex': '1 1 auto',
    'minWidth': '0',
    'width': '100%',
    'position': 'relative'
}

UPLOAD_BUTTON = {
    'width': '300px',
    'height': '150px',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'cursor': 'pointer',
    'backgroundColor': 'white',
    'transition': 'all 0.3s ease',
    ':hover': {
        'borderColor': PRIMARY_COLOR,
        'backgroundColor': '#f8f9fa'
    }
}

UPLOAD_ICON = {
    'fontSize': '48px',
    'color': MUTED_TEXT_COLOR,
    'marginBottom': '10px'
}

FILES_CONTAINER = {
    'marginTop': '10px',
    'display': 'flex',
    'flexWrap': 'wrap',
    'gap': '10px'
}

FILE_INFO = {
    'padding': '8px 12px',
    'backgroundColor': 'white',
    'borderRadius': BORDER_RADIUS,
    'border': BORDER_STYLE,
    'fontSize': '14px',
    'display': 'flex',
    'alignItems': 'center',
    'gap': '8px'
} 

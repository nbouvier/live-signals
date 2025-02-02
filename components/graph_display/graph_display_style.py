"""
This module contains styles for the graph display component.
"""

from styles import (
    BACKGROUND_COLOR,
    BORDER_STYLE,
    BORDER_RADIUS,
    MUTED_TEXT_COLOR,
    FONT_SIZE_LARGE
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
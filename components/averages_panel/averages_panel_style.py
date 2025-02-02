"""
This module contains styles for the averages panel component.
"""

from styles import (
    PRIMARY_COLOR,
    SPACING_MEDIUM,
    SPACING_SMALL,
    SPACING_LARGE,
    FONT_SIZE_NORMAL,
    BORDER_RADIUS
)

CONTAINER = {
    'flex': '0 0 300px'
}

HEADER = {
    'marginTop': '0',
    'marginBottom': SPACING_MEDIUM
}

CONTENT = {
    'marginBottom': SPACING_MEDIUM
}

INDICATOR_CONTAINER = {
    'display': 'flex',
    'alignItems': 'center',
    'marginBottom': SPACING_MEDIUM
}

SELECTION_INDICATOR = {
    'width': '20px',
    'height': '20px',
    'borderRadius': '50%',
    'display': 'inline-block',
    'marginRight': SPACING_MEDIUM
}

INDICATOR_LABEL = {
    'fontSize': FONT_SIZE_NORMAL
}

CALCULATE_BUTTON = {
    'backgroundColor': PRIMARY_COLOR,
    'color': 'white',
    'padding': f'{SPACING_SMALL} {SPACING_MEDIUM}',
    'border': 'none',
    'borderRadius': BORDER_RADIUS,
    'cursor': 'pointer',
    'width': '100%',
    'display': 'flex',
    'alignItems': 'center',
    'justifyContent': 'center',
    'gap': SPACING_SMALL,
    'fontSize': FONT_SIZE_NORMAL
}

BUTTON_ICON = {
    'marginRight': SPACING_SMALL
} 

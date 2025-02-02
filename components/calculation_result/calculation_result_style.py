"""
This module contains styles for the calculation result component.
"""

from styles import (
    BACKGROUND_COLOR,
    BORDER_RADIUS,
    BORDER_STYLE,
    SPACING_SMALL,
    SPACING_MEDIUM,
    SPACING_LARGE,
    MUTED_TEXT_COLOR,
    TRANSITION_NORMAL
)

CONTAINER = {
    'backgroundColor': BACKGROUND_COLOR,
    'padding': SPACING_MEDIUM,
    'borderRadius': BORDER_RADIUS,
    'marginBottom': SPACING_MEDIUM
}

HEADER = {
    'marginBottom': SPACING_MEDIUM
}

SECTION = {
    'marginBottom': SPACING_MEDIUM
}

DIVIDER = {
    'margin': f'{SPACING_MEDIUM} 0'
}

THICKNESS_INPUT = {
    'marginLeft': SPACING_SMALL,
    'width': '100px',
    'padding': SPACING_SMALL,
    'borderRadius': BORDER_RADIUS,
    'border': BORDER_STYLE
}

UNIT_LABEL = {
    'marginLeft': SPACING_SMALL,
    'color': MUTED_TEXT_COLOR
}

TOGGLE_BUTTON = {
    'backgroundColor': 'transparent',
    'border': 'none',
    'padding': f'{SPACING_SMALL} 0',
    'cursor': 'pointer',
    'display': 'flex',
    'alignItems': 'center',
    'width': '100%',
    'color': MUTED_TEXT_COLOR,
    'marginBottom': SPACING_SMALL
}

TOGGLE_ICON = {
    'marginRight': SPACING_SMALL,
    'transition': f'transform {TRANSITION_NORMAL}'
}

AVERAGES_CONTENT = {
    'maxHeight': '300px',
    'overflowY': 'auto',
    'display': 'none',
    'padding': SPACING_MEDIUM,
    'backgroundColor': 'white',
    'borderRadius': BORDER_RADIUS,
    'border': BORDER_STYLE
}

AVERAGE_ITEM = {
    'marginBottom': SPACING_SMALL
} 
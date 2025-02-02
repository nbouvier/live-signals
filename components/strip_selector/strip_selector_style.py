"""
This module contains styles for the strip selector component.
"""

from styles import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    WARNING_COLOR,
    BACKGROUND_COLOR,
    BORDER_RADIUS,
    BORDER_STYLE,
    SPACING_SMALL,
    SPACING_MEDIUM,
    SPACING_LARGE,
    FONT_SIZE_NORMAL,
    Z_INDEX_OVERLAY,
    TRANSITION_NORMAL,
    SHADOW_MEDIUM
)

STRIP_SELECTOR = {
    'display': 'grid',
    'gridTemplateColumns': 'repeat(auto-fill, minmax(100px, 1fr))',
    'gap': SPACING_SMALL,
    'maxHeight': 'calc(100vh - 190px)',
    'overflowY': 'auto',
    'padding': SPACING_MEDIUM,
    'border': BORDER_STYLE,
    'borderRadius': BORDER_RADIUS,
    'backgroundColor': BACKGROUND_COLOR,
    'margin': f'{SPACING_MEDIUM} 0'
}

BUTTON = {
    'backgroundColor': SECONDARY_COLOR,
    'color': 'white',
    'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
    'border': 'none',
    'borderRadius': BORDER_RADIUS,
    'margin': SPACING_SMALL,
    'cursor': 'pointer',
    'fontSize': FONT_SIZE_NORMAL
}

BUTTON_CONTAINER = {
    'display': 'flex',
    'gap': SPACING_MEDIUM,
    'marginBottom': SPACING_MEDIUM
}

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

TOGGLE_BUTTON = {
    'position': 'fixed',
    'top': SPACING_MEDIUM,
    'left': SPACING_MEDIUM,
    'zIndex': Z_INDEX_OVERLAY + 1,
    'backgroundColor': PRIMARY_COLOR,
    'color': 'white',
    'padding': f'{SPACING_MEDIUM} {SPACING_LARGE}',
    'border': 'none',
    'borderRadius': BORDER_RADIUS,
    'cursor': 'pointer',
    'fontSize': FONT_SIZE_NORMAL,
    'boxShadow': SHADOW_MEDIUM
}

UNSELECT_BUTTON = {
    **BUTTON,
    'backgroundColor': WARNING_COLOR
}

STRIP_LABEL = {
    'display': 'block',
    'padding': SPACING_SMALL,
    'backgroundColor': 'white',
    'borderRadius': BORDER_RADIUS,
    'margin': SPACING_SMALL,
    'cursor': 'pointer',
    'transition': f'background-color {TRANSITION_NORMAL}',
    ':hover': {'backgroundColor': '#e6e6e6'}
} 

"""
This module contains styles for the fit graph component.
"""

from styles import (
    MUTED_TEXT_COLOR,
    SPACING_MEDIUM,
    FONT_SIZE_NORMAL
)

CONTAINER = {
    'marginTop': SPACING_MEDIUM
}

GRAPH = {
    'height': '400px'
}

NO_DATA_MESSAGE = {
    'textAlign': 'center',
    'color': MUTED_TEXT_COLOR,
    'marginTop': SPACING_MEDIUM,
    'fontSize': FONT_SIZE_NORMAL
}

LEGEND = {
    'yanchor': 'top',
    'y': 0.99,
    'xanchor': 'right',
    'x': 0.99
}

MARGIN = {
    'l': 50,
    'r': 50,
    't': 50,
    'b': 50
}

EXPERIMENTAL_MARKER = {
    'color': 'orange',
    'symbol': 'triangle-up',
    'size': 10
}

FIT_LINE = {
    'color': 'black',
    'dash': 'dash'
} 

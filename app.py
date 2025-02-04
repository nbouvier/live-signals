"""
Main application file that initializes and runs the Dash application.
"""

import numpy as np
from dash import Dash
from data_processing import read_bin_file
from layout import create_layout
from callbacks import register_callbacks

def main():
    # Initialize the Dash app
    app = Dash(
        __name__,
        external_stylesheets=[
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
        ]
    )

    # Create the layout
    app.layout = create_layout()

    # Register callbacks
    register_callbacks(app)

    # Run the app
    if __name__ == '__main__':
        app.run(debug=True)

main() 

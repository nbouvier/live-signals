"""
Main application file that initializes and runs the Dash application.
"""

import numpy as np
from dash import Dash
from data_processing import read_bin_file, create_figure
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

    # Read the data
    path = r"C:\Users\nelbo\Bureau\Github\nbouvier\live-signals\data\4T_Al_Cu_step_fant_3_4_5_cm_VREF_UC_10000_sans_colli_MRT.bin"
    dt = np.dtype("uint16")
    with open(path, "rb") as f:
        data = f.read()
    zdata = np.frombuffer(data, dt)

    # Get time values and strip responses
    time_values, raw_strip_resp = read_bin_file(zdata)

    # Create the layout
    app.layout = create_layout(time_values, raw_strip_resp, create_figure)

    # Register callbacks
    register_callbacks(app, time_values, raw_strip_resp)

    # Run the app
    if __name__ == '__main__':
        app.run(debug=True)

main() 
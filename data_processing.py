"""
This module contains functions for reading and processing binary data files.
"""

import numpy as np
import plotly.graph_objects as go

def read_bin_file(zdata):
    """Read and process binary data file."""
    # correspondence of QDC number and strip number file
    correspondence_table_file = r"C:\Users\nelbo\Bureau\Github\nbouvier\live-signals\data\add_piste.txt"
    pf = open(correspondence_table_file, "r")
    correspondence_table = pf.readlines()

    # number of measurements
    nb_mes = np.size(zdata) // 309

    # time conversion (integration time = 10 ms + 0.5 ms of dead time)
    time_values = [event * 10.5 for event in range(nb_mes)]

    # strips responses matrix (line = strips, columns = strip responses)
    raw_strip_resp = np.zeros((153, nb_mes))

    # 17 first strips on the missing diamond => 0 response
    for strip_num in range(18, 153):
        corresponding_QDC_num = int(correspondence_table[strip_num])
        for event in range(nb_mes):
            raw_strip_resp[strip_num, event] = np.uint32(
                ((zdata[3 + corresponding_QDC_num * 2 + event * 309]) << 16)
                + (zdata[4 + corresponding_QDC_num * 2 + event * 309])
                >> 6
            )
            
    return time_values, raw_strip_resp

def create_figure(time_values, raw_strip_resp, selected_strips=None):
    """Create a plotly figure with the strip responses."""
    # Create figure with single plot (no subplots)
    fig = go.Figure()

    # Add traces for each strip
    for strip_num in range(18, 153):
        if selected_strips is None or strip_num in selected_strips:
            fig.add_scatter(
                x=time_values,
                y=raw_strip_resp[strip_num, :],
                name=f'Strip {strip_num}',
                mode='lines'
            )

    # Update layout
    fig.update_layout(
        title_x=0.5,
        xaxis=dict(
            title="Time (ms)",
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1s", step="second", stepmode="backward"),
                    dict(count=5, label="5s", step="second", stepmode="backward"),
                    dict(count=10, label="10s", step="second", stepmode="backward"),
                    dict(step="all", label="All")
                ])
            ),
            domain=[0, 0.95]
        ),
        yaxis_title="Strip response",
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            x=1,
            y=1,
            xanchor='left',
            yanchor='top'
        ),
        height=800,
        dragmode='select',
        selectdirection='h',
        modebar=dict(
            remove=['lasso2d']
        ),
        margin=dict(r=50)
    )

    return fig 
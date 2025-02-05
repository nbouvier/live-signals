"""
This module contains functions for reading and processing binary data files.
"""

import base64
import numpy as np
import plotly.graph_objects as go
from models import FileData

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

def create_figure(time_values, raw_strip_resp, selected_strips=None, calculation_results=None):
    """Create a plotly figure with the strip responses and selection rectangles."""
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
    
    # Add rectangles for previous selections
    if calculation_results:
        for idx, result in enumerate(calculation_results):
            if result.start_time is not None and result.end_time is not None:                
                # Get y-range for the rectangle
                y_min = min(raw_strip_resp[selected_strips, :].min() if selected_strips else raw_strip_resp[18:153, :].min(),
                          raw_strip_resp[selected_strips, :].mean() if selected_strips else raw_strip_resp[18:153, :].mean())
                y_max = max(raw_strip_resp[selected_strips, :].max() if selected_strips else raw_strip_resp[18:153, :].max(),
                          raw_strip_resp[selected_strips, :].mean() if selected_strips else raw_strip_resp[18:153, :].mean())
                
                # Add selection rectangle
                fig.add_shape(
                    type="rect",
                    x0=result.start_time,
                    x1=result.end_time,
                    y0=y_min,
                    y1=y_max,
                    fillcolor=result.color,
                    line=dict(width=0),
                    layer="below"
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

def process_file(contents, filename):
    """Process uploaded file and return FileData object."""
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    # Convert to numpy array
    dt = np.dtype("uint16")
    zdata = np.frombuffer(decoded, dt)
    
    # Process the data
    time_values, raw_strip_resp = read_bin_file(zdata)
    
    return FileData(filename, time_values, raw_strip_resp)

def create_multi_file_figure(files, selected_strips, calculation_results):
    """Create a figure with multiple files."""
    fig = go.Figure()
    
    # Add traces for each file, sorted by strip number
    traces = []
    # Sort selected strips numerically
    sorted_strips = sorted(selected_strips)
    
    for strip_num in sorted_strips:
        for file_data in files:
            # Add time offset to each time value
            adjusted_time = [t + file_data.time_offset for t in file_data.time_values]
            traces.append({
                'x': adjusted_time,
                'y': file_data.raw_strip_resp[strip_num, :],
                'name': f'Strip {strip_num} - File {file_data.id}',
                'mode': 'lines'
            })
    
    # Add traces in order (they're already sorted by strip number)
    for trace in traces:
        fig.add_scatter(**trace)
    
    # Add rectangles for calculations (if needed)
    if calculation_results:
        for result in calculation_results:
            if result.start_time is not None and result.end_time is not None:
                # Get y-range for the rectangle
                y_min = min(min(f.raw_strip_resp[sorted_strips, :].min() for f in files),
                          min(f.raw_strip_resp[sorted_strips, :].mean() for f in files))
                y_max = max(max(f.raw_strip_resp[sorted_strips, :].max() for f in files),
                          max(f.raw_strip_resp[sorted_strips, :].mean() for f in files))
                
                fig.add_shape(
                    type="rect",
                    x0=result.start_time,
                    x1=result.end_time,
                    y0=y_min,
                    y1=y_max,
                    fillcolor=result.color,
                    line=dict(width=0),
                    layer="below"
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
            yanchor='top',
            traceorder='normal'  # Keep traces in the order they were added
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

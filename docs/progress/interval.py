import dash_mantine_components as dmc
from dash import Input, Output, dcc, html, callback

component = html.Div(
    [
        dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
        dmc.Progress(id="progress", size="xl"),
    ]
)


@callback(
    Output("progress", "value"),
    Output("progress", "label"),
    Output("progress", "color"),
    Input("progress-interval", "n_intervals"),
)
def update_progress(n):
    # do some processing here
    progress = min(n % 110, 100)
    color = "red"
    if progress >= 20:
        color = "blue"
    if progress >= 40:
        color = "cyan"
    if progress >= 70:
        color = "teal"
    if progress == 100:
        color = "green"
    return progress, f"{progress} %", color

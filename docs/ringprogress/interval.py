import dash_mantine_components as dmc
from dash import Input, Output, dcc, html, callback, no_update
from dash_iconify import DashIconify

component = html.Div(
    [
        dcc.Interval(id="ring-progress-interval", n_intervals=0, interval=500),
        dmc.RingProgress(id="ring-progress", sections=[{"value": 0, "color": "red"}]),
    ]
)


@callback(
    Output("ring-progress", "sections"),
    Output("ring-progress", "label"),
    Input("ring-progress-interval", "n_intervals"),
)
def update_progress(n):
    # do some processing here
    progress = 5 * min(n % 26, 20)
    color = "indigo" if progress != 100 else "green"
    label = dmc.Text(f"{progress}%", color="indigo")
    if progress == 100:
        label = dmc.ThemeIcon(
            DashIconify(icon="radix-icons:check", width=30),
            radius="xl",
            size="xl",
            color="green",
            variant="light",
        )
    return [{"value": progress, "color": color}], [dmc.Center(label)]

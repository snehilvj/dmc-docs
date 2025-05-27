import dash_mantine_components as dmc
from dash import callback, Input, Output

component = dmc.Stack([
    dmc.TimeGrid(
        timeRangeData={"startTime": "10:00", "endTime": "21:00", "interval": "01:00"},
        withSeconds=False,
        simpleGridProps={
            "type": "container",
            "cols": {"base": 1, "180px": 2, "320px": 3},
            "spacing": "xs",
        },
        value="10:00:00",
        id="time-grid"
    ),
    dmc.Text(id="time-grid-out")
])

@callback(
    Output("time-grid-out", "children"),
    Input("time-grid", "value")
)
def update(value):
    return f"You selected: {value}"

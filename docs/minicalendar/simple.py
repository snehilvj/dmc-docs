import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Stack([
    dmc.MiniCalendar(
        defaultDate="2025-01-02",
        value="2025-01-03",
        id="mini-calendar"
    ),
    dmc.Text(id="mini-calendar-date", m="md")
])

@callback(
    Output("mini-calendar-date", "children"),
    Input("mini-calendar", "value"),
)
def update(d):
    return f"You selected: {d}"
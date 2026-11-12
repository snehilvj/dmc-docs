
from datetime import datetime, timedelta

import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import events

today = datetime.now().date()
tomorrow = today + timedelta(days=1)

component = dmc.Box([
    dmc.Text(id="schedule-date-view-out", mb="sm"),
    dmc.Divider(mb="md"),
    dmc.Schedule(
        id="schedule-date-view",
        events=events,
        date=tomorrow,
        view="month"
    )
])

@callback(
    Output("schedule-date-view-out", "children"),
    Input("schedule-date-view", "date"),
    Input("schedule-date-view", "view")
)
def schedule_date_view(date, view):
    return f"Selected date: {date} Selected view: {view}"


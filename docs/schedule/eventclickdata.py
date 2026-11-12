import json
import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from .data import events


component = dmc.Box([
    dmc.Schedule(events=events, id="schedule-clickdata"),
    dmc.Modal(
        id="event-modal",
        title="Event details",
        centered=True,
        children=dmc.CodeHighlight(
            id="event-data",
            language="json",
            code="{}",
        ),
    ),
])

@callback(
    Output("event-modal", "opened"),
    Output("event-data", "code"),
    Input("schedule-clickdata", "eventClickData"),
    prevent_initial_call=True,
)
def show_event(event):
    if not event:
        return False, "{}"

    return True, json.dumps(event, indent=2, default=str)
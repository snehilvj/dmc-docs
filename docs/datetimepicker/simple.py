import dash_mantine_components as dmc
from dash import Input, Output, html, callback, no_update


component = html.Div(
    [
        dmc.DateTimePicker(
            id="datetime-picker",
            label="Start Date and time",
            description="You can also provide a description",
            w=250,
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-datetime"),
    ]
)


@callback(Output("selected-datetime", "children"), Input("datetime-picker", "value"))
def update_output(d):
    return f"You have selected {d}"

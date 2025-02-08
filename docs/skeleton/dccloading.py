
import time
import dash_mantine_components as dmc
from dash import  Input, Output,  html, callback, dcc

component = html.Div(
    [
        dcc.Loading(
            children=html.Div([
                dmc.Text("Initial data", id="dccloading-div"),
                dmc.Text("The data only takes 200ms to update, but `delay_hide` is set to 1000ms to prevent flashing.")
            ]),
            delay_hide=1000,
            custom_spinner = dmc.Skeleton(
                visible=True,
                h="100%"
            ),
        ),
        dmc.Button("Update!", id="dccloading-button"),
    ]
)

@callback(
    Output("dccloading-div", "children"),
    Input("dccloading-button", "n_clicks"),
    prevent_initial_call=True
)
def update_graph(n):
    time.sleep(.2)
    return f"Data updated {n} times"


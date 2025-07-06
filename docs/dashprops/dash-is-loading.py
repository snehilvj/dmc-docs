from dash import  Input, Output, callback
import dash_mantine_components as dmc
import time


component = dmc.Stack([
    dmc.Title(" Dash Spinner Loader Showcase", order=2),

    dmc.Card([
        dmc.Select(
            label="Pulse Loader",
            placeholder="Choose an option...",
            data=["A", "B", "C"],
            id="dash-is-loading-input-1"
        ),
        dmc.Text(id="dash-is-loading-output-1", className="output-example-loading",  py="lg")
    ],
        className="pulse-loader",
        withBorder=True
    ),

    dmc.Card([
        dmc.Select(
            label="Ring Loader",
            placeholder="Choose an option...",
            data=["A", "B", "C"],
            id="dash-is-loading-input-2"
        ),
        dmc.Text(id="dash-is-loading-output-2", className="output-example-loading", py="lg")
    ], className="ring-loader", withBorder=True),

    dmc.Card([
        dmc.Select(
            label="Bounce Loader",
            placeholder="Choose an option...",
            data=["A", "B", "C"],
            id="dash-is-loading-input-3"
        ),
        dmc.Text(id="dash-is-loading-output-3", className="output-example-loading",  py="xl")
    ], className="bounce-loader"),


])

@callback(Output("dash-is-loading-output-1", "children"), Input("dash-is-loading-input-1", "value"))
def update_output1(value):
    time.sleep(2)
    return f"You selected: {value}"


@callback(Output("dash-is-loading-output-2", "children"), Input("dash-is-loading-input-2", "value"))
def update_output2(value):
    time.sleep(2)
    return f"You selected: {value}"


@callback(Output("dash-is-loading-output-3", "children"), Input("dash-is-loading-input-3", "value"))
def update_output3(value):
    time.sleep(2)
    return f"You selected: {value}"



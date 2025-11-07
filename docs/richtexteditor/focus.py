
import dash_mantine_components as dmc
from dash import  Input, Output, callback, ctx, no_update

component =  dmc.Box([
    dmc.Group([
        dmc.Button("Focus Start", id="rte-btn-focus-start"),
        dmc.Button("Focus End", id="rte-btn-focus-end"),
        dmc.Button("Blur", id="rte-btn-blur"),
    ]),
    dmc.RichTextEditor(
        id="rte-focus",
        html="<p>Click the buttons to control focus.</p>",
    ),
])


@callback(
    Output("rte-focus", "focus"),
    Input("rte-btn-focus-start", "n_clicks"),
    Input("rte-btn-focus-end", "n_clicks"),
    Input("rte-btn-blur", "n_clicks"),
    prevent_initial_call=True
)
def control_focus(start, end, blur):
    if not ctx.triggered:
        return no_update

    button_id = ctx.triggered_id
    if button_id == "rte-btn-focus-start":
        return "start"
    elif button_id == "rte-btn-focus-end":
        return "end"
    elif button_id == "rte-btn-blur":
        return False

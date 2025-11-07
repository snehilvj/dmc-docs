import requests
from dash import Input, Output, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Box([
    dmc.Button("Get rejection reason", id="new-reason-btn", mb="lg"),
    dmc.Group([
        dmc.Text(id="reason-text", mt=10),
        dmc.CopyButton(
            target_id="reason-text",
            children=DashIconify(icon="fa-regular:copy"),
            copiedChildren=DashIconify(icon="fa-regular:check-circle"),
            color="blue",
            copiedColor="teal",
            variant="outline",
            size="xs"
        )
    ], align="flex-start",  wrap="nowrap",)
])

@callback(
    Output("reason-text", "children"),
    Input("new-reason-btn", "n_clicks"),
    running=[(Output("new-reason-btn", "loading"), True, False)],
)
def fetch_reason(_):
    try:
        res = requests.get("https://naas.isalman.dev/no")
        res.raise_for_status()
        return res.json().get("reason", "No reason found.")
    except Exception:
        return "No reason. Just No."

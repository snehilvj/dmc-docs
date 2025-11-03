import dash_mantine_components as dmc
from dash import Input, Output, callback

component = dmc.Box([
    dmc.Select(
        id="copy-select",
        data=["Job A", "Job B", "Job C"],
        value="Job A",
        label="Select Job",
        description="Results are copied to the clipboard"
    ),
    dmc.CopyButton(
        id="copy-trigger",
        style={"visibility": "hidden"},
        value=""
    )
])

@callback(
    Output("copy-trigger", "value"),
    Output("copy-trigger", "triggerCopy"),
    Input("copy-select", "value")
)
def update_clipboard(v):
    return f"Results from {v}", True
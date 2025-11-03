
import dash_mantine_components as dmc
from dash import  Input, Output, callback

component = dmc.Box([
    dmc.Switch(
        id="rte-toggle-editable",
        label="Editable",
        checked=True,
    ),
    dmc.RichTextEditor(
        id="rte-editable",
        html="<p>This editor can be toggled between editable and read-only mode.</p>",
        editable=True,
        toolbar={
            "controlsGroups": [
                [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strikethrough",
                    "CodeBlock"
                ],
            ],
        },
    ),
])

@callback(
    Output("rte-editable", "editable"),
    Input("rte-toggle-editable", "checked"),
)
def toggle_editable(checked):
    return checked

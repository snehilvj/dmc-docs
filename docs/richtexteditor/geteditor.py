
import dash_mantine_components as dmc
from dash import Dash, Input, Output, clientside_callback

component = dmc.Box([
    dmc.RichTextEditor(
        id="get-editor-id",
        toolbar={
                "controlsGroups": [
                    [
                        "Bold",
                        "Italic",
                        "Underline",
                        "Strikethrough",
                    ],
                ],
            },
        html="<p>Try typing some text in this editor. Click the button below to see your character and word count.</p>"
    ),
    dmc.Button("Get Stats", id="btn-rte-stats", n_clicks=0),
    dmc.Box(id="stats"),
])

clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            const editor = dash_mantine_components.getEditor('get-editor-id');
            if (editor) {
                const text = editor.getText();
                const chars = text.length;
                const words = text.split(/\\s+/).filter(Boolean).length;
                return `Characters: ${chars} | Words: ${words}`;
            }
        }
        return dash_clientside.no_update;
    }
    """,
    Output("stats", "children"),
    Input("btn-rte-stats", "n_clicks"),
)


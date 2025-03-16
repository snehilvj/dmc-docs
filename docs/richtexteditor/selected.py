from dash import Input, Output, html, callback
import dash_mantine_components as dmc

component = html.Div(
    [
        dmc.RichTextEditor(
            html="<p>Welcome to the editor.</p><p><strong>Select some text</strong></p>",
            extensions=[
                "StarterKit",
            ],
            toolbar={
                "controlsGroups": [
                    [
                        "Bold",
                        "Italic",
                        "Underline",
                        "Strikethrough",
                        "Highlight",
                    ],
                ]
            },
            id="rte",
        ),
        dmc.Box(id="rte-selected", mt="lg"),
    ]
)


@callback(Output("rte-selected", "children"), Input("rte", "selected"))
def update_content(content: str):
    return f"Your selected text: {content}"

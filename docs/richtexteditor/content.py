from dash import Input, Output, html, callback
import dash_mantine_components as dmc

content = """<h2 style="text-align: center;">Welcome to Mantine rich text editor</h2>"""

component = html.Div(
    [
        dmc.RichTextEditor(
            html=content,
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
                    ],
                ],
            },
            id="rte-content",
        ),
        dmc.Text("html content:", mt="lg"),
        dmc.Paper(id="rte-content-html", withBorder=True, mb="lg", p="md"),
        dmc.Text("json content:"),
        dmc.Paper(id="rte-content-json", withBorder=True, p="md"),
    ]
)


@callback(Output("rte-content-html", "children"), Input("rte-content", "html"))
def update_content(content: str):
    return f"{content}"


@callback(Output("rte-content-json", "children"), Input("rte-content", "json"))
def update_content(content: str):
    return f"{content}"

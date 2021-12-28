import importlib

import dash_mantine_components as dmc
from dash import dcc, html
from dash.dependencies import Input, Output

import callbacks
from app import app
from components.header import header

components = [
    "Accordion",
    "Affix",
    "Alert",
    "Badge",
    "Button",
    "Checkbox",
    "Chips",
    "DatePicker",
    "DateRangePicker",
    "Divider",
    "Drawer",
    "Image",
    "Modal",
    # "MultiSelect",
    "Notifications",
    # "Paper",
    # "Prism",
    # "Progress",
    # "RadioGroup",
    # "SegmentedControl",
    # "Select",
    # "Slider",
    # "Spoiler",
    # "Switch",
    # "Table",
    # "Tabs",
    # "Text",
    # "TextInput",
    # "Title",
    # "Tooltip",
]


app.layout = dmc.Container(
    size="lg",
    children=[
        header,
        dcc.Location(id="url"),
        dmc.Space(h=20),
        dmc.Grid(
            children=[
                dmc.Col(
                    span=3,
                    children=[
                        dmc.Group(
                            children=[
                                dmc.Anchor(cmp, href=f"/{cmp.lower()}")
                                for cmp in components
                            ],
                            direction="column",
                            spacing="xs",
                        )
                    ],
                ),
                dmc.Col(span=9, id="page-content"),
            ]
        ),
    ],
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def page(pathname):
    if pathname == "/":
        pathname = "Accordion"
    else:
        pathname = pathname.lstrip("/")

    try:
        module = importlib.import_module(f"components.{pathname.lower()}")
        return html.Div(
            children=[
                dmc.Text(
                    module.title,
                    size="xl",
                    style={"fontSize": 30, "marginBottom": 10},
                ),
                module.layout,
                dmc.Space(h=50),
                dmc.Text("Keyword arguments", color="dimmed"),
                dmc.Space(h=10),
                dmc.Prism(
                    language="git",
                    code=module.doc,
                    noCopy=True,
                    style={"whiteSpace": "pre-wrap"},
                ),
                dmc.Space(h=50),
            ],
        )
    except ImportError:
        return dmc.Alert(
            "Sorry, this page doesn't exist right now!", color="red", show=True
        )


if __name__ == "__main__":
    app.run_server(debug=True)

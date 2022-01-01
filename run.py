import importlib

import dash_mantine_components as dmc
from dash import dcc, html
from dash.dependencies import Input, Output

import callbacks
from app import app
from components.header import header

server = app.server

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

    module = importlib.import_module(f"components.{pathname.lower()}")
    return html.Div(
        children=[module.layout],
    )


if __name__ == "__main__":
    app.run_server(debug=True)

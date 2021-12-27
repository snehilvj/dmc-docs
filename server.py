from os import initgroups, path
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
from components.header import header
import importlib
import inspect

app = Dash(__name__, suppress_callback_exceptions=True)

components = [
    "Accordion",
    "Affix",
    "Alert",
    "Anchor",
    "Badge",
    "Blockquote",
    "Breadcrumbs",
    "Button",
    "Center",
    "Checkbox",
    "Chips",
    "Container",
    "DatePicker",
    "DateRangePicker",
    "Divider",
    "Drawer",
    "Grid",
    "Group",
    "Image",
    "Modal",
    "MultiSelect",
    "NotificationHandler",
    "NotificationsProvider",
    "Paper",
    "Prism",
    "Progress",
    "RadioGroup",
    "SegmentedControl",
    "Select",
    "SimpleGrid",
    "Skeleton",
    "Slider",
    "Space",
    "Spoiler",
    "Switch",
    "Table",
    "Tabs",
    "Text",
    "TextInput",
    "Title",
    "Tooltip",
]


app.layout = dmc.Container(
    style={"padding": "20px 120px"},
    fluid=True,
    children=[
        header,
        dcc.Location(id="url"),
        dmc.Space(h=20),
        dmc.Grid(
            children=[
                dmc.Col(
                    span=2,
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
                dmc.Col(span=10, id="page-content"),
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
        return dmc.Group(
            direction="column",
            grow=True,
            children=[
                dmc.Text(
                    module.title,
                    size="xl",
                    style={"fontSize": 30},
                ),
                dmc.Text("Example"),
                module.layout,
                dmc.Space(),
                dmc.Text("Keyword arguments"),
                dmc.Prism(
                    language="markdown",
                    code=module.doc,
                    noCopy=True,
                    style={"whiteSpace": "pre-wrap"},
                ),
            ],
        )
    except ImportError:
        return dmc.Alert(
            "Sorry, this page doesn't exist right now!", color="red", show=True
        )


if __name__ == "__main__":
    app.run_server(debug=True)

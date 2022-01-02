import importlib

import dash_mantine_components as dmc
from dash import dcc, html
from dash.dependencies import Input, Output

import callbacks
from app import app
from components.header import header
from home_layout import home_layout
from utils import components

server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        header,
        dmc.Container(
            size="lg",
            style={"paddingTop": 80},
            children=[
                dmc.Space(h=20),
                dmc.Grid(
                    children=[
                        dmc.Col(
                            span=3,
                            children=[
                                dmc.Anchor("Getting Started", href="/"),
                                dmc.Space(h=20),
                                dmc.Text("Components", color="dimmed"),
                                dmc.Space(h=10),
                                dmc.Group(
                                    children=[
                                        dmc.Anchor(cmp, href=f"/{cmp.lower()}")
                                        for cmp in components
                                    ],
                                    direction="column",
                                    spacing="xs",
                                ),
                            ],
                        ),
                        dmc.Col(span=9, id="page-content"),
                    ]
                ),
            ],
        ),
    ]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def page(pathname):
    if pathname == "/":
        return home_layout
    pathname = pathname.lstrip("/")
    module = importlib.import_module(f"components.{pathname}")
    return module.layout


if __name__ == "__main__":
    app.run_server(debug=True)

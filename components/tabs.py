import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

tabs = html.Div(
    [
        create_component_title("Tabs"),
        dmc.Tabs(
            [
                dmc.Tab(label="Tab 1", children=[dmc.Text("Tab 1")]),
                dmc.Tab(label="Tab 2", children=[dmc.Text("Tab 2")]),
                dmc.Tab(label="Tab 3", children=[dmc.Text("Tab 3")]),
            ],
            position="center",
        ),
        dmc.Space(h=20),
        dmc.Tabs(
            [
                dmc.Tab(label="Tab 1", children=[dmc.Text("Tab 1")]),
                dmc.Tab(label="Tab 2", children=[dmc.Text("Tab 2")]),
                dmc.Tab(label="Tab 3", children=[dmc.Text("Tab 3")]),
            ],
            active=2,
            variant="outline",
        ),
        dmc.Space(h=20),
        dmc.Tabs(
            [
                dmc.Tab(label="Tab 1", children=[dmc.Text("Tab 1")]),
                dmc.Tab(label="Tab 2", children=[dmc.Text("Tab 2")]),
                dmc.Tab(label="Tab 3", children=[dmc.Text("Tab 3")]),
            ],
            orientation="vertical",
            position="center",
        ),
        dmc.Space(h=30),
    ]
)

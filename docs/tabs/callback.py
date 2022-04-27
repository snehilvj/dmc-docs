import dash_mantine_components as dmc
from dash import Input, Output, html, callback

from lib.utils import create_graph

component = html.Div(
    [
        dmc.Tabs(
            id="tabs-example",
            active=1,
            children=[
                dmc.Tab(label="Tab One"),
                dmc.Tab(label="Tab Two"),
            ],
        ),
        html.Div(id="tabs-content"),
    ]
)


@callback(Output("tabs-content", "children"), Input("tabs-example", "active"))
def render_content(active):
    if active == 0:
        return [dmc.Text("Tab One selected"), create_graph()]
    else:
        return [dmc.Text("Tab Two selected"), create_graph()]

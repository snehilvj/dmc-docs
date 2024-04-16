import dash_mantine_components as dmc
from dash import Input, Output, html, callback

from lib.utils import create_graph

component = html.Div(
    [
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.TabsTab("Tab one", value="1"),
                        dmc.TabsTab("Tab two", value="2"),
                    ]
                ),
            ],
            id="tabs-example",
            value="1",
        ),
        html.Div(id="tabs-content", style={"paddingTop": 10}),
    ]
)


@callback(Output("tabs-content", "children"), Input("tabs-example", "value"))
def render_content(active):
    if active == "1":
        return [dmc.Text("Tab One selected"), create_graph()]
    else:
        return [dmc.Text("Tab Two selected"), create_graph()]

from dash import Dash, html
from dash import Input, Output, callback
import dash_mantine_components as dmc

app = Dash()


def make_section(i, name):
    return dmc.Box(
        [
            dmc.Title(children=f"{name} {i}", id=f"section-{i}", order=3),
            dmc.Space(h=200),
        ],
        p="lg",
    )


app.layout = dmc.MantineProvider(
    dmc.AppShell(
        dmc.AppShellMain(
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
                    value="1",
                    id="tabs",
                ),
                dmc.Box(id="tabs-content"),
                dmc.AppShellAside(
                    [
                        dmc.Title("Table of Contents", order=4, mt=60),
                        dmc.ScrollArea(
                            dmc.TableOfContents(
                                target_id="tabs-content",
                                selector="#tabs-content :is( h2, h3, h4)",
                            )
                        ),
                    ]
                ),
            ],
            p="md",
        )
    )
)


@callback(
    Output("tabs-content", "children"),
    Input("tabs", "value"),
)
def render_content(active):
    if active == "1":
        return html.Div([make_section(i, "Section") for i in range(30)])
    return html.Div([make_section(i, "Topic") for i in range(30)])


if __name__ == "__main__":
    app.run(debug=True)

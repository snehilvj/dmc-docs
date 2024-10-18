from dash import callback, Input, Output
import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Button("Toggle Content", id="collapse-root-btn", n_clicks=0, mb="sm", size="lg"),
    dmc.Collapse(
        children=dmc.Box([
            dmc.Text("Hello World!", mt="lg"),
            dmc.Button(
                "Toggle Content",
                id="collapse-inner-btn",
                n_clicks=0,
                variant="outline",
                size="sm",
                my="lg",
                ml="lg"
            ),
            dmc.Collapse(children= dmc.Text("Hello Nested Worlds!", ml="lg"), id="collapse-inner")
        ]),
        opened=False,
        id="collapse-root"
    )
])

@callback(
    Output("collapse-root", "opened"),
    Input("collapse-root-btn", "n_clicks"),
)
def update(n):
    if n % 2 == 0:
        return False
    return True


@callback(
    Output("collapse-inner", "opened"),
    Input("collapse-inner-btn", "n_clicks"),
)
def update(n):
    if n % 2 == 0:
        return False
    return True


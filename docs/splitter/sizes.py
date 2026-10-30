from dash import Dash, Input, Output,  callback, ctx
import dash_mantine_components as dmc

component = dmc.Box([
        dmc.Splitter(
        h=200,
        mb="md",
        classNames={"pane": "splitter-examples"},
        resetOnDoubleClick=True,
        id="splitter-sizes",
        children=[
            dmc.SplitterPane(
                "Panel A (50%)",
                id="panel-a",
                defaultSize=50,
                min=20,
                bg="blue",
            ),
            dmc.SplitterPane(
                "Panel B (50%)",
                id="panel-b",
                defaultSize=50,
                min=20,
                bg="teal",
            ),
        ],
    ),
    dmc.Button("30/70", id="button-30-70", mr="sm"),
    dmc.Button("50/50", id="button-50-50", mr="sm"),
    dmc.Button("70/30", id="button-70-30"),
])


@callback(
    Output("splitter-sizes", "sizes"),
    Input("button-30-70", "n_clicks"),
    Input("button-50-50", "n_clicks"),
    Input("button-70-30", "n_clicks"),
    prevent_initial_call=True
)
def handle_size_buttons_click(n_clicks_30_70, n_clicks_50_50, n_clicks_70_30):
    if ctx.triggered_id == "button-30-70":
        return [30, 70]
    elif ctx.triggered_id == "button-70-30":
        return [70, 30]
    else:
        return [50, 50]

@callback(
    Output("panel-a", "children"),
    Output("panel-b", "children"),
    Input("splitter-sizes", "sizes"),
    prevent_initial_call=True
)
def handle_size_change(sizes):
    sizes = sizes or [50, 50]
    return f"Panel A ({sizes[0]:.0f}%)", f"Panel B ({sizes[1]:.0f}%)"

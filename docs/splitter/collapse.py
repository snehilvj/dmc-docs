
import dash_mantine_components as dmc
from dash import Input, Output, State, callback

component = dmc.Box([
    dmc.Splitter(
        id="splitter-collapse",
        h=200,
        classNames={"pane": "splitter-examples"},
        children=[
            dmc.SplitterPane(
                "Collapsible sidebar",
                collapsible=True,
                defaultSize=30,
                min=20,
                bg="blue",
            ),
            dmc.SplitterPane(
                "Main content",
                defaultSize=70,
                min=30,
                bg="teal",
            ),
        ],
    ),
    dmc.Button("Toggle Sidebar", id="splitter-collapse-toggle-button", mt="md")
])

@callback(
    Output("splitter-collapse", "collapsed"),
    Input("splitter-collapse-toggle-button", "n_clicks"),
    State("splitter-collapse", "collapsed"),
    prevent_initial_call=True,
)
def toggle_sidebar(n_clicks, collapsed):
    return [0] if not collapsed or 0 not in collapsed else []

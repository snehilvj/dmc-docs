
import json
import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data

component = dmc.Stack([
    dmc.Tree(data=data, checkboxes=True, id="tree-checkboxes" ),
    dmc.CodeHighlight(id="checked-nodes", code="", language="json"),
])


@callback(
    Output("checked-nodes", "code"),
    Input("tree-checkboxes", "checked")
)
def update(checked):
    return  json.dumps( checked, indent=4)


import json
import dash_mantine_components as dmc
from dash import callback, Input, Output
import dash_iconify # necessary to import here in order to use in the renderNode function
from .data import data

component = dmc.Stack([
    dmc.Tree(
        data=data,
        levelOffset=23,
        expandOnClick=False,
        renderNode={"function": "myLeafCheckbox"},
        id="tree-checkboxes-renderNode" ),
    dmc.CodeHighlight(id="checked-nodes-renderNode", code="", language="json"),
])


@callback(
    Output("checked-nodes-renderNode", "code"),
    Input("tree-checkboxes-renderNode", "checked")
)
def update(checked):
    return  json.dumps( checked, indent=4)


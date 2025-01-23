

import json
import dash_mantine_components as dmc
from dash import  callback, Input, Output
from .data import data

component = dmc.Stack([
    dmc.Tree(
        data=data,
        expanded=[
            "node_modules",
            "node_modules/@mantine",
            "node_modules/@mantine/form",
            "node_modules/@mantine/form/index.d.ts",
        ],
        id="tree-expanded"
    ),
    dmc.CodeHighlight(id="expanded-nodes", code="", language="json"),
])


@callback(
    Output("expanded-nodes", "code"),
    Input("tree-expanded", "expanded")
)
def update(expanded):
    return  json.dumps( expanded, indent=4)

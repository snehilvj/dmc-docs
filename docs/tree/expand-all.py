
import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data

component = dmc.Box([
    dmc.SegmentedControl(
        id="tree-expand-all",
        data=["Expand All", "Collapse All"],
        value="Collapse All",
        mb="sm"
    ),

    dmc.Tree(
        data=data,
        id="tree-all"
    )
],p="lg")

@callback(
    Output("tree-all", "expanded"),
    Input("tree-expand-all", "value")
)
def update(value):
    if value=="Collapse All":
        return []
    return '*'

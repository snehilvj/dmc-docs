import dash_mantine_components as dmc

from lib.utils import create_graph

component = dmc.Tabs(
    [
        dmc.Tab(label="Tab one", children=create_graph()),
        dmc.Tab(label="Tab two", children=create_graph()),
        dmc.Tab(label="Tab three", children=create_graph()),
    ]
)

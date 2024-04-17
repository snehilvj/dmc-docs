import dash_mantine_components as dmc

from lib.utils import create_graph

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Tab one", value="1"),
                dmc.TabsTab("Tab two", value="2"),
                dmc.TabsTab("Tab three", value="3"),
            ]
        ),
        dmc.TabsPanel(create_graph(), value="1"),
        dmc.TabsPanel(create_graph(), value="2"),
        dmc.TabsPanel(create_graph(), value="3"),
    ],
    value="1",
)

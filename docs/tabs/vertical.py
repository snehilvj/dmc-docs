import uuid

import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "placement",
        "component": "DemoSegmentedControl",
        "value": "right",
        "data": ["left", "right"],
    },
]


demo = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings"),
            ],
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery", px="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", px="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", px="xs"),
    ],
    value="gallery",
    orientation="vertical",
    placement="right",
)

component = create_configurator(demo, controls, center=False)

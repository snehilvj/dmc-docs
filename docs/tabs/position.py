import uuid

import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "position",
        "component": "Select",
        "data": ["left", "right", "center", "apart"],
        "value": "left",
    },
    {"property": "grow", "component": "Switch", "checked": False},
]

cid = str(uuid.uuid4())

demo = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings"),
            ],
            id=cid,
        ),
    ],
    value="gallery",
)

component = create_configurator(demo, controls, center=False, cid=cid)

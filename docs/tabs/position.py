import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-tabs-position"

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings"),
            ],
            id=TARGET_ID,
        ),
    ],
    value="gallery",
)


configurator = Configurator(target, TARGET_ID)

configurator.add_select("position", ["left", "right", "center", "apart"], "left")
configurator.add_switch("grow", False)

component = configurator.panel

import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-tabs-position"

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ],
            id=TARGET_ID,
        ),
    ],
    value="gallery",
)


configurator = Configurator(target, TARGET_ID)

configurator.add_select(
    "justify", ["flex-start", "center", "flex-end", "space-around"], "center"
)
configurator.add_switch("grow", False)

component = configurator.panel

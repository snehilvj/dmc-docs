import dash_mantine_components as dmc

from lib.configurator import Configurator

# to fix, target ID on tabsList
target = dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ],
        )

configurator = Configurator(target)

configurator.add_select(
    "justify", ["flex-start", "center", "flex-end", "space-around"], "center"
)
configurator.add_switch("grow", False)

component = dmc.Tabs(
    [
        configurator.panel
    ],
    value="gallery",
)


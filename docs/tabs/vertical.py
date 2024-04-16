import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-tabs-vertical"

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ],
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery", px="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", px="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", px="xs"),
    ],
    value="gallery",
    orientation="vertical",
    placement="right",
    id=TARGET_ID,
)


configurator = Configurator(target, TARGET_ID)

configurator.add_select("placement", ["left", "right"], "right")


component = configurator.panel

import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ]
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery", pt="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", pt="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", pt="xs"),
    ],
    value="gallery",
)

configurator = Configurator(target)

configurator.add_colorpicker("color", "red")
configurator.add_segmented_control(
    "variant", ["default", "outline", "pills"], "default"
)
configurator.add_slider("radius", "md")
configurator.add_segmented_control(
    "orientation", ["horizontal", "vertical"], "horizontal"
)

component = configurator.panel

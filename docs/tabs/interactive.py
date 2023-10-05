import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-tabs"

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings"),
            ]
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery", pt="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", pt="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", pt="xs"),
    ],
    value="gallery",
    id=TARGET_ID,
)


configurator = Configurator(target, TARGET_ID)
configurator.add_colorpicker("color", "indigo")
configurator.add_segmented_control(
    "variant", ["default", "outline", "pills"], "default"
)
configurator.add_slider("radius", "md")
configurator.add_segmented_control(
    "orientation", ["horizontal", "vertical"], "horizontal"
)

component = configurator.panel

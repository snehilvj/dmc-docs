import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "DemoSegmentedControl",
        "data": ["default", "outline", "pills"],
        "value": "default",
    },
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {
        "property": "orientation",
        "component": "DemoSegmentedControl",
        "data": ["horizontal", "vertical"],
        "value": "horizontal",
    },
]

demo = dmc.Tabs(
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
)

component = create_configurator(demo, controls, center=False)

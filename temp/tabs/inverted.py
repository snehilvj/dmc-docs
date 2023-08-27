import dash_mantine_components as dmc

component = dmc.Tabs(
    [
        dmc.TabsPanel("Gallery tab content", value="gallery", pb="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", pb="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", pb="xs"),
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings", ml="auto"),
            ]
        ),
    ],
    value="gallery",
    inverted=True,
)

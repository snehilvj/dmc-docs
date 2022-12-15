import dash_mantine_components as dmc

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings", ml="auto"),
            ]
        ),
    ],
    value="gallery",
)

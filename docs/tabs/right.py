import dash_mantine_components as dmc

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings", ml="auto"),
            ]
        ),
    ],
    value="gallery",
)

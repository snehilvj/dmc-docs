import dash_mantine_components as dmc

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ],
            grow=True,
            bd="1px solid var(--mantine-color-default-border)"
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery"),
        dmc.TabsPanel("Messages tab content", value="messages"),
        dmc.TabsPanel("Settings tab content", value="settings"),
    ],
    color="green.3",
    autoContrast=True,
    variant="pills",
    value="gallery",
)

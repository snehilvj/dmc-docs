import dash_mantine_components as dmc

component = dmc.Tabs(
    color="teal",
    value="first",
    children=[
        dmc.TabsList(
            children=[
                dmc.TabsTab("Teal tab", value="first"),
                dmc.TabsTab("Blue tab", value="second", color="blue"),
            ]
        ),
        dmc.TabsPanel(
            "First tab color is teal, it gets this value from context",
            value="first",
            pt="xs",
        ),
        dmc.TabsPanel(
            "Second tab color is blue, it gets this value from props, props have the priority and will override context value",
            value="second",
            pt="xs",
        ),
    ],
)

import dash_mantine_components as dmc

def make_tabs(variant):
    return dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ]
        ),
        dmc.TabsPanel(f'variant="{variant}"', value="gallery"),
        dmc.TabsPanel("Messages tab content", value="messages"),
        dmc.TabsPanel("Settings tab content", value="settings"),
    ],
    variant=variant,
    value="gallery",
    m="md"
)

component = dmc.Stack([
    make_tabs("default"),
    make_tabs("outline"),
    make_tabs("pills")
])
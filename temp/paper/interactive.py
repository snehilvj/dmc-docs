import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "p", "component": "DemoSlider", "value": "lg"},
    {"property": "shadow", "component": "DemoSlider", "value": "sm"},
    {"property": "withBorder", "component": "Switch", "checked": False},
]

demo = dmc.Paper(
    children=[
        dmc.Text(
            "Paper is the most basic ui component. Use it to create cards, dropdowns, "
            "modals and other components that require background with shadow "
        )
    ],
    radius="sm",
    p="lg",
    shadow="sm",
    withBorder=False,
)

component = create_configurator(demo, controls)

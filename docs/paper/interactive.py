import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Paper(
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

configurator = Configurator(target)
configurator.add_slider("radius", "sm")
configurator.add_slider("p", "lg")
configurator.add_slider("shadow", "sm")
configurator.add_switch("withBorder", False)

component = configurator.panel

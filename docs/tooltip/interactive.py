import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Tooltip(
        label="Tooltip",
        opened=True,
        withArrow=True,
        children=[dmc.Button("Button with tooltip", variant="outline", size="lg")],
    )

configurator = Configurator(target, center_component=True)

configurator.add_colorpicker("color", "red")
configurator.add_slider("radius", "sm")
configurator.add_select(
    "position",
    [
        "top",
        "right",
        "bottom",
        "left",
        "top-end",
        "top-start",
        "right-end",
        "right-start",
        "bottom-end",
        "bottom-start",
        "left-end",
        "left-start",
    ],
    "top",
)
configurator.add_switch("withArrow", True)

component = configurator.panel

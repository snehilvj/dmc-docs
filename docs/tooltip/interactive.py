import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-tooltip"

target = dmc.Center(
    dmc.Tooltip(
        id=TARGET_ID,
        label="Tooltip",
        opened=True,
        withArrow=True,
        children=[dmc.Button("Tooltip", variant="outline", size="xl")],
    )
)

configurator = Configurator(target, TARGET_ID)
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

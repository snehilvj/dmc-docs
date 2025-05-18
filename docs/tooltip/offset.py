import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-tooltip-offset"

target = dmc.Center(
    dmc.Tooltip(
        id=TARGET_ID,
        label="Tooltip",
        opened=True,
        withArrow=False,
        children=[dmc.Button("Button with tooltip")],
    )
)

configurator = Configurator(target, TARGET_ID, "Tooltip")
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
configurator.add_number_slider("offset", min=-50, max=50,  value=0)

component = configurator.panel

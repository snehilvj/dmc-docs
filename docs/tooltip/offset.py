import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Tooltip(
        label="Tooltip",
        opened=True,
        withArrow=False,
        children=[dmc.Button("Button with tooltip")],
    )

configurator = Configurator(target, center_component=True)

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

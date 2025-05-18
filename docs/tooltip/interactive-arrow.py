import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Tooltip(
        label="Tooltip",
        position="top-start",
        opened=True,
        withArrow=True,
        children=[dmc.Button("Button with tooltip")],
    )

configurator = Configurator(target, center_component=True)

configurator.add_segmented_control("arrowPosition", ["center", "side"], "center")
configurator.add_number_slider("arrowOffset", min=5, max=50, value=5)
configurator.add_number_slider("arrowSize", min=1, max=15, value=8)
configurator.add_number_slider("arrowRadius", min=1, max=10, value=3)
component = configurator.panel

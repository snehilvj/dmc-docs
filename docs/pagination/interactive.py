import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Pagination(
    total=10,
    size="md",
    radius="sm",
    withControls=True,
    withEdges=False,
)

configurator = Configurator(target)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "md")
configurator.add_slider("radius", "sm")
configurator.add_switch("withControls", True)
configurator.add_switch("withEdges", False)

component = configurator.panel

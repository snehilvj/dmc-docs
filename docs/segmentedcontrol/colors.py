import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.SegmentedControl(
    value="Angular",
    data=["React", "Angular", "Svelte", "Vue"],
    color="indigo",
)

configurator = Configurator(target)

configurator.add_colorpicker("color", "indigo")

component = configurator.panel

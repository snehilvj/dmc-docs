import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-segmentedControl-color"

target = dmc.SegmentedControl(
    value="Angular",
    data=["React", "Angular", "Svelte", "Vue"],
    color="indigo",
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "indigo")

component = configurator.panel

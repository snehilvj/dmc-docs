import dash_mantine_components as dmc

from components.configurator import Configurator


target = dmc.SegmentedControl(
    value="Angular", data=["React", "Angular", "Svelte", "Vue"]
)

configurator = Configurator(target)

configurator.add_segmented_control(
    "orientation", ["horizontal", "vertical"], "horizontal"
)
configurator.add_switch("fullWidth", False)

component = configurator.panel

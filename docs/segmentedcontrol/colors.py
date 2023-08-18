import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [{"property": "color", "component": "ColorPicker", "value": "#5c7cfa"}]

demo = dmc.SegmentedControl(
    value="Angular", data=["React", "Angular", "Svelte", "Vue"], color="indigo"
)

component = create_configurator(demo, controls)

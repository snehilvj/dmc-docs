import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "orientation",
        "component": "SegmentedControl",
        "value": "horizontal",
        "data": ["horizontal", "vertical"],
    },
    {"property": "fullWidth", "component": "Switch", "checked": False},
]

demo = dmc.SegmentedControl(value="Angular", data=["React", "Angular", "Svelte", "Vue"])

component = create_configurator(demo, controls, center=False)

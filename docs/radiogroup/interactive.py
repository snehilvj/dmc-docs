import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "orientation",
        "component": "SegmentedControl",
        "data": ["horizontal", "vertical"],
        "value": "horizontal",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "md"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "required", "component": "Switch", "checked": False},
]

demo = dmc.RadioGroup(
    size="sm",
    spacing="md",
    label="Select your favorite framework/library",
    description="This is anonymous",
    data=[{"label": x, "value": x} for x in ["React", "Angular", "Dash", "Django"]],
    value="React",
)

component = create_configurator(demo, controls)

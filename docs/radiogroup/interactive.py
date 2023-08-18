import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "orientation",
        "component": "DemoSegmentedControl",
        "data": ["horizontal", "vertical"],
        "value": "horizontal",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "md"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "required", "component": "Switch", "checked": False},
]

demo = dmc.RadioGroup(
    [dmc.Radio(x, value=x) for x in ["React", "Angular", "Dash", "Django"]],
    size="sm",
    spacing="md",
    label="Select your favorite framework/library",
    description="This is anonymous",
    value="React",
)

component = create_configurator(demo, controls)

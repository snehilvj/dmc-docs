import dash_mantine_components as dmc
from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "withControls", "component": "Switch", "checked": True},
    {"property": "withEdges", "component": "Switch", "checked": False},
]

demo = dmc.Pagination(
    total=10,
    size="md",
    radius="sm",
    withControls=True,
    withEdges=False,
)

component = create_configurator(demo, controls)

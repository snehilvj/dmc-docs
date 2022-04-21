import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {
        "property": "variant",
        "component": "SegmentedControl",
        "data": ["outline", "filled"],
        "value": "outline",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "xs"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "xl"},
]

demo = dmc.Chips(
    value="React",
    data=[{"label": x, "value": x} for x in ["React", "Django", "Dash", "Vue"]],
    variant="outline",
)

component = create_configurator(demo, controls)

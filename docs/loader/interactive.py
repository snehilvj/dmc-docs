import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {
        "property": "variant",
        "component": "SegmentedControl",
        "data": ["oval", "bars", "dots"],
        "value": "oval"
    },
]

demo = dmc.Loader()

component = create_configurator(demo, controls)

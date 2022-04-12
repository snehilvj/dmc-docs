import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
]

demo = dmc.Avatar(src="/assets/avatar.jpeg")

component = create_configurator(demo, controls)

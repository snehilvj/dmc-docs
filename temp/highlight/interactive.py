import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "highlightColor", "component": "ColorPicker", "value": "#94d92e"},
]

demo = dmc.Highlight("Highlight this, definitely this and also this!", highlight="this")

component = create_configurator(demo, controls)

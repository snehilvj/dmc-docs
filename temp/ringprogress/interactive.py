import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "size",
        "component": "NumberInput",
        "value": 120,
        "min": 0,
        "step": 10,
    },
    {"property": "thickness", "component": "NumberInput", "value": 12, "min": 0},
    {"property": "roundCaps", "component": "Switch", "checked": False},
]

demo = dmc.RingProgress(
    size=120,
    thickness=12,
    sections=[
        {"value": 40, "color": "red"},
        {"value": 15, "color": "yellow"},
        {"value": 15, "color": "violet"},
    ],
)

component = create_configurator(demo, controls)

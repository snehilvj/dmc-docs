import copy

from lib.configurator import create_configurator
from docs.timeline.simple import component as timeline

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "radius", "component": "DemoSlider", "value": "xl"},
    {
        "property": "active",
        "component": "NumberInput",
        "value": 1,
        "min": 0,
        "max": 3,
        "step": 1,
    },
    {"property": "reverseActive", "component": "Switch", "checked": False},
    {
        "property": "lineWidth",
        "component": "NumberInput",
        "value": 2,
        "min": 1,
        "max": 8,
        "step": 1,
    },
    {
        "property": "bulletSize",
        "component": "NumberInput",
        "value": 15,
        "min": 12,
        "max": 30,
        "step": 1,
    },
    {
        "property": "align",
        "component": "DemoSegmentedControl",
        "data": ["left", "right"],
        "value": "left",
    },
]

demo = copy.deepcopy(timeline)
component = create_configurator(demo, controls)

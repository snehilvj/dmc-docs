import dash_mantine_components as dmc
from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "lg"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "spacing", "component": "DemoSlider", "value": "xs"},
    {"property": "withControls", "component": "Switch", "checked": True},
    {"property": "withEdges", "component": "Switch", "checked": False},
    {
        "property": "total",
        "component": "NumberInput",
        "description": "Total Number of Pages",
        "value": 10,
        "min": 1,
        "max": 15,
        "step": 1,
    },
    {
        "property": "boundaries",
        "component": "NumberInput",
        "description": "Adjust amount of elements visible on left/right edges",
        "value": 5,
        "min": 1,
        "max": 10,
        "step": 1,
    },
    {
        "property": "direction",
        "component": "SegmentedControl",
        "data": [
            {"value": "row", "label": "Row"},
            {"value": "column", "label": "Column"},
        ],
        "value": "row",
    },
]

demo = dmc.Pagination(
    total=10,
    # direction="column",
    # withControls=False,
    # withEdges=False,
    grow=True,
    align="stretch",
)

component = create_configurator(demo, controls)

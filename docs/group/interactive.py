import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "position",
        "component": "Select",
        "data": [
            "left",
            "right",
            "center",
            "apart",
        ],
        "value": "left",
    },
    {
        "property": "direction",
        "component": "SegmentedControl",
        "data": ["row", "column"],
        "value": "row",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "md"},
    {
        "property": "grow",
        "component": "Switch",
        "checked": False,
    },
]

demo = dmc.Group(
    [dmc.Button(val, variant="outline", fullWidth=True) for val in ["1", "2", "3"]],
    position="left",
)

component = create_configurator(demo, controls, center=False)

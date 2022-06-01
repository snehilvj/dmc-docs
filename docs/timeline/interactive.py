import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker"},
    {"property": "radius", "component": "DemoSlider", "value": "md"},
    {
        "property": "active",
        "component": "NumberInput",
        "value": 3,
        "min": 0,
        "max": 5,
        "step": 1,
    },
    {
        "property": "reverseAction",
        "component": "Switch",
        "checked": False,
    },
    {
        "property": "lineWidth",
        "component": "NumberInput",
        "value": 4,
        "min": 1,
        "max": 8,
        "step": 1,
    },
    {
        "property": "bulletSize",
        "component": "NumberInput",
        "value": 20,
        "min": 12,
        "max": 30,
        "step": 1,
    },
    {
        "property": "align",
        "component": "SegmentedControl",
        "data": ["Left", "Right"],
        "value": "Left",
    },
]


demo = dmc.Timeline(
    [
        dmc.TimelineItem(
            "pip install dash-mantine-components",
        ),
        dmc.TimelineItem(
            [
                "Check out our  ",
                dmc.Anchor(
                    "documentation",
                    href="https://www.dash-mantine-components.com/",
                    underline=False,
                ),
            ],
        ),
        dmc.TimelineItem(
            [
                "Join our ",
                dmc.Anchor(
                    "Discord", href="https://discord.gg/KuJkh4Pyq5", underline=False
                ),
                " Community",
            ],
        ),
        dmc.TimelineItem("Make something cool"),
        dmc.TimelineItem(
            "Share your app in show-and-tell",
        ),
    ],
    active=3,
)

component = create_configurator(demo, controls)

import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "type",
        "component": "SegmentedControl",
        "data": ["unordered", "ordered"],
        "value": "unordered",
    },
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {
        "property": "withPadding",
        "component": "Switch",
        "checked": False,
    },
]

demo = dmc.List(
    [
        dmc.ListItem("Join our Discord Community."),
        dmc.ListItem("Install python virtual environment."),
        dmc.ListItem(["Install npm dependencies with ", dmc.Code("npm install")]),
        dmc.ListItem(["Add your new component in ", dmc.Code("src/lib/components.")]),
        dmc.ListItem(
            "Raise a PR, including an example to reproduce the changes contributed by the PR."
        ),
    ],
    type="unordered",
)

component = create_configurator(demo, controls, center=False)

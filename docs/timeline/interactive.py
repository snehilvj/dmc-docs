import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "radius", "component": "DemoSlider", "value": "md"},
    {
        "property": "active",
        "component": "NumberInput",
        "value": 1,
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
        "data": ["left", "right"],
        "value": "left",
    },
]


demo = dmc.Timeline(
    [
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've created 'fix-notification' branch",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("2 hours ago", size="xs"),
            ],
            title="New Branch",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've pushed 23 commits to 'fix-notification' branch",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("42 minutes ago", size="xs"),
            ],
            title="Commits",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've submitted a pull request 'Fix incorrect notification message (#178)'",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("32 minutes ago", size="xs"),
            ],
            title="Pull Request",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "Snehil left a comment on your pull request",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("12 minutes ago", size="xs"),
            ],
            title="Code Review",
        ),
    ],
    active=3,
)

component = create_configurator(demo, controls)


"""

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

        dmc.TimelineItem("Make something cool"),
        dmc.TimelineItem(
            "Share your app in show-and-tell",
        ),
        dmc.TimelineItem(
            [
                "Join our ",
                dmc.Anchor(
                    "Discord", href="https://discord.gg/KuJkh4Pyq5", underline=False
                ),
                " Community if you would like to contribute to dmc",
            ],
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've created 'fix-notification' branch", color="dimmed", size="sm"),
                dmc.Text("2 hours ago", size="xs")
            ],
            title="New Branch",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've pushed 23 commits to 'fix-notification' branch", color="dimmed", size="sm"),
                dmc.Text("42 minutes ago", size="xs")
            ],
            title="Commits",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've submitted a pull request 'Fix incorrect notification message (#178)'", color="dimmed", size="sm"),
                dmc.Text("32 minutes ago", size="xs")
            ],
            title="Pull Request",
            lineVariant="dashed"
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "Snehil left a comment on your pull request", color="dimmed", size="sm"),
                dmc.Text("12 minutes ago", size="xs")
            ],
            title="Code Review",

        )
    ],
    active=3,
)


"""

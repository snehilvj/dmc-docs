import dash_mantine_components as dmc
from components.configurator import Configurator

TARGET_ID = "interactive-timeline"

target = dmc.Timeline(
    id=TARGET_ID,
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        dmc.TimelineItem(
            title="New Branch",
            children=[
                dmc.Text(
                    [
                        "You've created new branch ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                        " from master",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Commits",
            children=[
                dmc.Text(
                    [
                        "You've pushed 23 commits to ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Pull Request",
            lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "You've submitted a pull request ",
                        dmc.Anchor(
                            "Fix incorrect notification message (#178)",
                            href="#",
                            size="sm",
                        ),
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    [
                        dmc.Anchor(
                            "AnnMarieW",
                            href="https://github.com/AnnMarieW",
                            size="sm",
                        ),
                        " left a comment on your pull request",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
            title="Code Review",
        ),
    ],
)


configurator = Configurator(target, TARGET_ID)
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("radius", "xl")
configurator.add_number_input("active", 2, **{"min": -1, "max": 3})
configurator.add_switch("reverseActive", False)
configurator.add_number_input("lineWidth", 4, **{"min": 0, "max": 8})
configurator.add_number_input("bulletSize", 20, **{"min": 12, "max": 30, "step": 2})
configurator.add_segmented_control("align", ["left", "right"], "left")

component = configurator.panel

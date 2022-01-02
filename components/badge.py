import dash_mantine_components as dmc
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
    OnlyComponentBlock,
    SubText,
    Title,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Badge.__doc__)

layout = html.Div(
    children=[
        ComponentName("Badge"),
        ComponentDescription(description),
        Title("Interactive Demo"),
        SubText(
            "You can customize your badge and then just copy the auto generated code."
        ),
        OnlyComponentBlock(
            [
                dmc.Grid(
                    align="stretch",
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Badge(
                                        "Badge",
                                        id="badge-demo",
                                        variant="filled",
                                        color="blue",
                                        radius="xl",
                                        size="md",
                                    ),
                                    style={"height": 240},
                                )
                            ],
                            span=7,
                        ),
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Group(
                                        direction="column",
                                        grow=True,
                                        children=[
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Variant", size="sm"),
                                                    dmc.Select(
                                                        id="variant-badge-demo",
                                                        value="filled",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "light",
                                                                "filled",
                                                                "outline",
                                                                "dot",
                                                                "gradient",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Color", size="sm"),
                                                    dmc.Select(
                                                        id="color-badge-demo",
                                                        value="blue",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "dark",
                                                                "gray",
                                                                "red",
                                                                "pink",
                                                                "grape",
                                                                "violet",
                                                                "indigo",
                                                                "blue",
                                                                "cyan",
                                                                "teal",
                                                                "green",
                                                                "lime",
                                                                "yellow",
                                                                "orange",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Radius", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="radius-badge-demo",
                                                        value="xl",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": s,
                                                                "label": s,
                                                            }
                                                            for s in [
                                                                "xs",
                                                                "sm",
                                                                "md",
                                                                "lg",
                                                                "xl",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Size", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="size-badge-demo",
                                                        value="md",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": s,
                                                                "label": s,
                                                            }
                                                            for s in [
                                                                "xs",
                                                                "sm",
                                                                "md",
                                                                "lg",
                                                                "xl",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Children", size="sm"),
                                                    dmc.TextInput(
                                                        id="children-badge-demo",
                                                        value="Badge",
                                                    ),
                                                ],
                                            ),
                                        ],
                                    )
                                )
                            ],
                            span=5,
                        ),
                    ],
                )
            ],
        ),
        html.Div(id="badge-code-output"),
        dmc.Space(h=50),
        ComponentBlock(
            title="With Gradient",
            caption="You can also customize the gradient fill of the badge.",
            code="""import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.Badge(
            "Indigo cyan",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
        ),
        dmc.Badge(
            "Lime green",
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
        ),
        dmc.Badge(
            "Teal blue",
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
        ),
        dmc.Badge(
            "Orange red",
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
        ),
        dmc.Badge(
            "Grape pink",
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
        ),
    ]
)""",
        ),
        ComponentBlock(
            title="Badge within a Button",
            caption=dcc.Markdown("You can put badge in a button's `children`."),
            code="""import dash_mantine_components as dmc

component = dmc.Button(
    children=[
        "Notifications", dmc.Badge("2", radius="sm", style={"marginLeft": 7})
    ]
)""",
        ),
        ComponentReference(apidocs),
    ]
)

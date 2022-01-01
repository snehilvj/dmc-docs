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

description, apidocs = parse_apidocs(dmc.Button.__doc__)

layout = html.Div(
    children=[
        ComponentName("Button"),
        ComponentDescription(description),
        Title("Interactive Demo"),
        SubText(
            "You can customize your Button and then just copy the auto generated code."
        ),
        OnlyComponentBlock(
            [
                dmc.Grid(
                    align="stretch",
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Button(
                                        "Settings",
                                        id="button-demo",
                                        variant="filled",
                                        color="blue",
                                        radius="sm",
                                        size="sm",
                                        loading=False,
                                        compact=False,
                                    ),
                                    style={"height": 275},
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
                                                        id="variant-button-demo",
                                                        value="filled",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "filled",
                                                                "outline",
                                                                "light",
                                                                "gradient",
                                                                "white",
                                                                "default",
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
                                                        id="color-button-demo",
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
                                                        id="radius-button-demo",
                                                        value="sm",
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
                                                        id="size-button-demo",
                                                        value="sm",
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
                                            dmc.SimpleGrid(
                                                cols=2,
                                                children=[
                                                    dmc.Switch(
                                                        label="Loading",
                                                        id="loading-button-demo",
                                                        checked=False,
                                                    ),
                                                    dmc.Switch(
                                                        label="Compact",
                                                        id="compact-button-demo",
                                                        checked=False,
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Children", size="sm"),
                                                    dmc.TextInput(
                                                        id="children-button-demo",
                                                        value="Settings",
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
        html.Div(id="button-code-output"),
        dmc.Space(h=50),
        ComponentBlock(
            title="With Gradient",
            caption="You can also customize the gradient fill of the button.",
            code="""import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.Button(
            "Indigo cyan",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
        ),
        dmc.Button(
            "Lime green",
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
        ),
        dmc.Button(
            "Teal blue",
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
        ),
        dmc.Button(
            "Orange red",
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
        ),
        dmc.Button(
            "Grape pink",
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
        ),
    ]
)""",
        ),
        ComponentBlock(
            title="Full width button",
            caption=dcc.Markdown("Pass `fullWidth=True` for a full width button."),
            code="""import dash_mantine_components as dmc

component = dmc.Button("Click to open the app", fullWidth=True, variant="outline")""",
        ),
        ComponentReference(apidocs),
    ]
)

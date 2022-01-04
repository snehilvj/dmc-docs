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
from data import parse_apidocs

description, apidocs = parse_apidocs(dmc.Chips.__doc__)

layout = html.Div(
    children=[
        ComponentName("Chips"),
        ComponentDescription(description),
        Title("Interactive Demo"),
        SubText(
            "You can customize your Chips and then just copy the auto generated code."
        ),
        OnlyComponentBlock(
            [
                dmc.Grid(
                    align="stretch",
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Chips(
                                        id="chips-demo",
                                        data=[
                                            {"value": "react", "label": "React"},
                                            {"value": "ng", "label": "Angular"},
                                            {"value": "svelte", "label": "Svelte"},
                                            {"value": "vue", "label": "Vue"},
                                        ],
                                        value="react",
                                        color="blue",
                                        radius="xl",
                                        size="sm",
                                        spacing="xs",
                                        variant="outline",
                                        multiple=False,
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
                                                    dmc.Text("Color", size="sm"),
                                                    dmc.Select(
                                                        id="color-chips-demo",
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
                                                    dmc.Text("Variant", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="variant-chips-demo",
                                                        value="outline",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "outline",
                                                                "label": "Outline",
                                                            },
                                                            {
                                                                "value": "filled",
                                                                "label": "Filled",
                                                            },
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Radius", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="radius-chips-demo",
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
                                                    dmc.Text("Spacing", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="spacing-chips-demo",
                                                        value="xs",
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
                                                        id="size-chips-demo",
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
                                            dmc.Switch(
                                                label="Multiple",
                                                id="multiple-chips-demo",
                                                checked=False,
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
        html.Div(id="chips-code-output"),
        dmc.Space(h=50),
        ComponentBlock(
            title="Callbacks",
            caption=dcc.Markdown(
                "The `value` property is a list of items if `multiple=True` else a single item"
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Chips(
        id="chips-values",
        data = [
            {"value": "react", "label": "React"},
            {"value": "ng", "label": "Angular"},
            {"value": "svelte", "label": "Svelte"},
            {"value": "vue", "label": "Vue"},
        ],
        value="react",
    ),
    dmc.Space(h=20),
    dmc.Text(id="chips-values-output"),
])


@app.callback(
    Output("chips-values-output", "children"),
    Input("chips-values", "value"),
)
def chips_values(value):
    return value""",
        ),
        ComponentReference(apidocs),
    ]
)

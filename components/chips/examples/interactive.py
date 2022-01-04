import dash_mantine_components as dmc
from dash import html, Input, Output

data_string = """data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ]"""

component = html.Div(
    [
        dmc.SimpleGrid(
            cols=6,
            spacing="xl",
            children=[
                dmc.Text(label, size="sm", style={"marginBottom": 3})
                for label in ["Color", "Variant", "Radius", "Size", "Spacing", ""]
            ],
        ),
        dmc.SimpleGrid(
            cols=6,
            spacing="xl",
            children=[
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
                dmc.Switch(
                    label="Multiple",
                    id="multiple-chips-demo",
                    checked=False,
                ),
            ],
        ),
        dmc.SimpleGrid(
            cols=2,
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
                ),
                dmc.Prism(
                    id="chips-code-output",
                    code="",
                    language="python",
                    style={"marginTop": 20},
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("chips-code-output", "code"),
    Output("chips-demo", "variant"),
    Output("chips-demo", "color"),
    Output("chips-demo", "radius"),
    Output("chips-demo", "size"),
    Output("chips-demo", "multiple"),
    Output("chips-demo", "spacing"),
    Input("variant-chips-demo", "value"),
    Input("color-chips-demo", "value"),
    Input("radius-chips-demo", "value"),
    Input("size-chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
    Input("spacing-chips-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, multiple, spacing):
    return [
        f"""import dash_mantine_components as dmc

dmc.Chips(
    {data_string}
    color="{color}",
    radius="{radius}",
    size="{size}",
    spacing="{spacing}",
    variant="{variant}",
    multiple={multiple},
)""",
        variant,
        color,
        radius,
        size,
        multiple,
        spacing,
    ]


@app.callback(
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    return ["vue", "react"] if multiple else "react"

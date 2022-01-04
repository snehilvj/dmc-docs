import dash_mantine_components as dmc
from dash import html, Input, Output

component = html.Div(
    [
        dmc.SimpleGrid(
            cols=5,
            spacing="xl",
            children=[
                dmc.Text(label, size="sm", style={"marginBottom": 3})
                for label in ["Variant", "Color", "Radius", "Size", "Children"]
            ],
        ),
        dmc.SimpleGrid(
            cols=5,
            spacing="xl",
            children=[
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
                dmc.TextInput(
                    id="children-badge-demo",
                    value="Badge",
                ),
            ],
        ),
        dmc.SimpleGrid(
            cols=2,
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
                ),
                dmc.Prism(
                    id="badge-code-output",
                    code="",
                    language="python",
                    style={"marginTop": 20},
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("badge-code-output", "code"),
    Output("badge-demo", "variant"),
    Output("badge-demo", "color"),
    Output("badge-demo", "radius"),
    Output("badge-demo", "size"),
    Output("badge-demo", "children"),
    Input("variant-badge-demo", "value"),
    Input("color-badge-demo", "value"),
    Input("radius-badge-demo", "value"),
    Input("size-badge-demo", "value"),
    Input("children-badge-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, children):
    return [
        f"""import dash_mantine_components as dmc

dmc.Badge(
    "{children}",
    variant="{variant}",
    color="{color}",
    radius="{radius}",
    size="{size}"
)""",
        variant,
        color,
        radius,
        size,
        children,
    ]

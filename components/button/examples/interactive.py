import dash_mantine_components as dmc
from dash import html, Input, Output

component = html.Div(
    [
        dmc.SimpleGrid(
            cols=6,
            spacing="xl",
            children=[
                dmc.Text(label, size="sm", style={"marginBottom": 3})
                for label in ["Variant", "Color", "Radius", "Size", "Children", ""]
            ],
        ),
        dmc.SimpleGrid(
            cols=6,
            spacing="xl",
            children=[
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
                dmc.TextInput(
                    id="children-button-demo",
                    value="Settings",
                ),
                dmc.Switch(
                    label="Compact",
                    id="compact-button-demo",
                    checked=False,
                ),
            ],
        ),
        dmc.SimpleGrid(
            cols=2,
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
                ),
                dmc.Prism(
                    id="button-code-output",
                    code="",
                    language="python",
                    style={"marginTop": 20},
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("button-code-output", "code"),
    Output("button-demo", "variant"),
    Output("button-demo", "color"),
    Output("button-demo", "radius"),
    Output("button-demo", "size"),
    Output("button-demo", "compact"),
    Output("button-demo", "children"),
    Input("variant-button-demo", "value"),
    Input("color-button-demo", "value"),
    Input("radius-button-demo", "value"),
    Input("size-button-demo", "value"),
    Input("compact-button-demo", "checked"),
    Input("children-button-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, compact, children):
    return [
        f"""import dash_mantine_components as dmc

dmc.Button(
    "{children}",
    variant="{variant}",
    color="{color}",
    radius="{radius}",
    size="{size}",
    compact={compact},
)""",
        variant,
        color,
        radius,
        size,
        compact,
        children,
    ]

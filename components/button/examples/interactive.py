import dash_mantine_components as dmc
from dash import html, Input, Output

from lib.blocks import DemoSelect, MantineThemeColorSwatches, DemoSlider

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
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
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="variant-button-demo",
                            value="filled",
                            label="Variant",
                            data=[
                                "filled",
                                "outline",
                                "light",
                                "gradient",
                                "white",
                                "default",
                            ],
                        ),
                        MantineThemeColorSwatches(id="color-button-demo"),
                        DemoSlider(
                            id="radius-button-demo", label="Radius", initial_value=2
                        ),
                        DemoSlider(
                            id="size-button-demo", label="Size", initial_value=2
                        ),
                        dmc.TextInput(
                            id="children-button-demo",
                            value="Settings",
                            label="Children",
                        ),
                        dmc.Switch(
                            label="Compact",
                            id="compact-button-demo",
                            checked=False,
                        ),
                        dmc.Switch(
                            label="Loading",
                            id="loading-button-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            id="button-code-output", code="", language="python", style={"marginTop": 30}
        ),
    ]
)


app.clientside_callback(
    """
    function(variant, color, radius, size, compact, loading, children) {
        return [
            `import dash_mantine_components as dmc

dmc.Button(
    "${children}",
    variant="${variant}",
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}"
    compact=${compact ? "True" : "False"},
    loading=${loading ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        compact,
        loading,
        children
        ];
    }
    """,
    Output("button-code-output", "code"),
    Output("button-demo", "variant"),
    Output("button-demo", "color"),
    Output("button-demo", "radius"),
    Output("button-demo", "size"),
    Output("button-demo", "compact"),
    Output("button-demo", "loading"),
    Output("button-demo", "children"),
    Input("variant-button-demo", "value"),
    Input("color-button-demo", "value"),
    Input("radius-button-demo", "drag_value"),
    Input("size-button-demo", "drag_value"),
    Input("compact-button-demo", "checked"),
    Input("loading-button-demo", "checked"),
    Input("children-button-demo", "value"),
)

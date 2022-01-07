import dash_mantine_components as dmc
from dash import html, Input, Output


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
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="variant-chips-demo",
                            value="filled",
                            label="Variant",
                            data=["filled", "outline"],
                        ),
                        MantineThemeColorSwatches(id="color-chips-demo"),
                        DemoSlider(
                            id="radius-chips-demo", label="Radius", initial_value=5
                        ),
                        DemoSlider(id="size-chips-demo", label="Size", initial_value=2),
                        DemoSlider(
                            id="spacing-chips-demo", label="Spacing", initial_value=1
                        ),
                        dmc.Switch(
                            label="Multiple",
                            id="multiple-chips-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            id="chips-code-output", code="", language="python", style={"marginTop": 30}
        ),
    ]
)


app.clientside_callback(
    """
    function(variant, color, radius, size, multiple, spacing) {
        return [
            `import dash_mantine_components as dmc

dmc.Chips(
    data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ],
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}",
    spacing="${window.sizeMap[spacing]}",
    variant="${variant}",
    multiple=${multiple ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        multiple,
        window.sizeMap[spacing]
        ];
    }
    """,
    Output("chips-code-output", "code"),
    Output("chips-demo", "variant"),
    Output("chips-demo", "color"),
    Output("chips-demo", "radius"),
    Output("chips-demo", "size"),
    Output("chips-demo", "multiple"),
    Output("chips-demo", "spacing"),
    Input("variant-chips-demo", "value"),
    Input("color-chips-demo", "value"),
    Input("radius-chips-demo", "drag_value"),
    Input("size-chips-demo", "drag_value"),
    Input("multiple-chips-demo", "checked"),
    Input("spacing-chips-demo", "drag_value"),
)


@app.callback(
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    return ["vue", "react"] if multiple else "react"

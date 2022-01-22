import dash_mantine_components as dmc
from dash import html, Input, Output

from lib.interactive import DemoSelect, MantineThemeColorSwatches, DemoSlider

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
            "", id="chips-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)

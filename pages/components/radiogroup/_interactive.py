import dash_mantine_components as dmc
from dash import html

from lib.interactive import MantineThemeColorSwatches, DemoSlider, DemoSegmentedControl

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.RadioGroup(
                            id="radio-demo",
                            data=[
                                {"value": "react", "label": "React"},
                                {"value": "ng", "label": "Angular"},
                                {"value": "svelte", "label": "Svelte"},
                                {"value": "vue", "label": "Vue"},
                            ],
                            value="react",
                            color="blue",
                            size="sm",
                            spacing="md",
                            label="Select your favorite framework/library",
                            description="This is anonymous",
                            required=True,
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSegmentedControl(
                            id="variant-radio-demo",
                            label="Variant",
                            values=["Horizontal", "Vertical"],
                            initial_value="horizontal",
                        ),
                        DemoSlider(
                            id="spacing-radio-demo", label="Spacing", initial_value=3
                        ),
                        DemoSlider(id="size-radio-demo", label="Size", initial_value=2),
                        MantineThemeColorSwatches(id="color-radio-demo"),
                        dmc.Switch(
                            label="Required",
                            id="required-radio-demo",
                            checked=True,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="radio-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)

import dash_mantine_components as dmc
from dash import Output, Input, html

from lib.interactive import MantineThemeColorSwatches

component = html.Div(
    [
        dmc.Group(
            position="apart",
            children=[
                dmc.Checkbox(
                    id="checkbox-color",
                    label="Use me as a boolean input",
                    checked=True,
                ),
                MantineThemeColorSwatches(id="color-checkbox-demo"),
            ],
        ),
        dmc.Prism(
            "",
            id="checkbox-code-output",
            language="python",
            style={"marginTop": 30},
        ),
    ]
)

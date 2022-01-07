import dash_mantine_components as dmc
from dash import Output, Input, html

from lib.blocks import MantineThemeColorSwatches

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
            id="checkbox-code-output",
            code="",
            language="python",
            style={"marginTop": 30},
        ),
    ]
)

app.clientside_callback(
    """
    function(color) {
        return [
            `import dash_mantine_components as dmc

dmc.Checkbox(
    label="Use me as a boolean input",
    checked=True,
    color="${window.colorMap[color]}"
)`,
        window.colorMap[color]
    ];
    }
    """,
    Output("checkbox-code-output", "code"),
    Output("checkbox-color", "color"),
    Input("color-checkbox-demo", "value"),
)

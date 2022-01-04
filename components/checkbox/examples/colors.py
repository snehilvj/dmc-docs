import dash_mantine_components as dmc
from dash import Output, Input

component = dmc.Group(
    position="apart",
    children=[
        dmc.Checkbox(
            id="checkbox-color",
            label="Use me as a boolean input",
            checked=True,
            color="green",
        ),
        dmc.Select(
            id="color-checkbox-demo",
            value="green",
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
)


@app.callback(
    Output("checkbox-color", "color"),
    Input("color-checkbox-demo", "value"),
)
def color_checkbox_demo(color):
    return color

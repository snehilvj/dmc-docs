from dash import Input, Output, callback
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Text("Click the same star to clear the rating", size="sm"),
        dmc.Rating(id="rating-clear", value=3, allowClear=True),
        dmc.Group(
            [
                dmc.Text("Current rating:", size="sm", c="dimmed"),
                dmc.Text(id="rating-clear-value", size="sm", fw=600, children="3"),
            ],
            gap="xs",
        ),
    ],
    gap="md",
    align="center",
)


@callback(
    Output("rating-clear-value", "children"),
    Input("rating-clear", "value"),
)
def update_rating(value):
    return "Not rated" if value == 0 else value


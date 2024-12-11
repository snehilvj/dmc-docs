
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html, Input, Output, callback, ALL

icon = DashIconify(icon="tabler:photo", width=14)

component = dmc.Box(
    [
        dmc.Text("Update justify prop:"),
        dmc.SegmentedControl(
            data=["center", "space-between"],
            value="center",
            id="button-justify",
            mb="lg"
        ),

        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            rightSection=icon,
            variant="default",
            id={"type":"button-justify", "index": 1}
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            variant="default",
            mt="md",
            id={"type": "button-justify", "index": 2}
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            rightSection=icon,
            variant="default",
            mt="md",
            id={"type": "button-justify", "index": 3}
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=html.Span(),  # Empty spacer
            rightSection=icon,
            variant="default",
            mt="md",
            id={"type": "button-justify", "index": 4}
        ),
    ]
)


@callback(
    Output({"type": "button-justify", "index": ALL}, "justify"),
    Input("button-justify", "value"),
)
def update_figure(value):
    return [value] * 4


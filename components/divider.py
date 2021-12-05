import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

divider = html.Div(
    [
        create_component_title("Divider"),
        dmc.Divider(label="Click on update button to refresh"),
        dmc.Space(h=20),
        dmc.Divider(
            label="This is a divider with centered content", labelPosition="center"
        ),
        dmc.Space(h=20),
        dmc.Divider(
            label="This is a dotted divider with content on the right",
            labelPosition="right",
            variant="dotted",
        ),
        dmc.Space(h=20),
    ]
)

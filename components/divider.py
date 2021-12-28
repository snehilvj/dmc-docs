import dash_mantine_components as dmc
from dash import html

title = "Divider"
doc = dmc.Divider.__doc__

layout = html.Div(
    children=[
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.Divider(),
        dmc.Space(h=20),
        dmc.Divider(
            variant="dashed",
        ),
        dmc.Space(h=20),
        dmc.Divider(
            variant="dotted",
        ),
        dmc.Space(h=50),
        dmc.Text("With label", color="dimmed"),
        dmc.Space(h=10),
        dmc.Divider(label="Click on update button to refresh"),
        dmc.Space(h=20),
        dmc.Divider(
            label="Divider with centered content and dashed variant",
            labelPosition="center",
            variant="dashed",
        ),
        dmc.Space(h=20),
        dmc.Divider(
            label="Divider with content on the right and dotted variant",
            labelPosition="right",
            variant="dotted",
        ),
        dmc.Space(h=50),
        dmc.Text("Sizes", color="dimmed"),
        dmc.Space(h=10),
        dmc.Divider(size="xs"),
        dmc.Space(h=20),
        dmc.Divider(size="sm"),
        dmc.Space(h=20),
        dmc.Divider(size="md"),
        dmc.Space(h=20),
        dmc.Divider(size="lg"),
        dmc.Space(h=20),
        dmc.Divider(size="xl"),
        dmc.Space(h=20),
        dmc.Divider(size=10),
    ]
)

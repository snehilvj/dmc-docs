import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Text("Extra small text", size="xs"),
        dmc.Text("Small text", size="sm"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Large text", size="lg"),
        dmc.Text("Extra large text", size="xl"),
        dmc.Text("Semi bold", weight=500),
        dmc.Text("Bold", weight=700),
        dmc.Text("Underlined", underline=True),
        dmc.Text("Red text", color="red"),
        dmc.Text("Blue text", color="blue"),
        dmc.Text("Gray text", color="gray"),
        dmc.Text("Uppercase", transform="uppercase"),
        dmc.Text("capitalized text", transform="capitalize"),
        dmc.Text("Aligned to center", align="center"),
        dmc.Text("Aligned to right", align="right"),
    ]
)

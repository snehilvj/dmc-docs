import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Text("Extra small text", size="xs"),
        dmc.Text("Small text", size="sm"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Large text", size="lg"),
        dmc.Text("Extra large text", size="xl"),
        dmc.Text("Semi bold", fw=500),
        dmc.Text("Bold", fw=700),
        dmc.Text("Underlined", td="underline"),
        dmc.Text("Red text", c="red"),
        dmc.Text("Blue text", c="blue"),
        dmc.Text("Gray text", c="gray"),
        dmc.Text("Uppercase", tt="uppercase"),
        dmc.Text("capitalized text", tt="capitalize"),
        dmc.Text("Aligned to center", ta="center"),
        dmc.Text("Aligned to right", ta="right"),
    ]
)

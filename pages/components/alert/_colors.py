import dash_mantine_components as dmc
from dash import html

message = "Something happened! You made a mistake and there is no going back!"

component = html.Div(
    [
        dmc.Alert(message, title="Primary", color="blue"),
        dmc.Space(h=10),  # no-prism
        dmc.Alert(message, title="Secondary", color="gray"),
        dmc.Space(h=10),  # no-prism
        dmc.Alert(message, title="Success!", color="green"),
        dmc.Space(h=10),  # no-prism
        dmc.Alert(message, title="Warning!", color="yellow"),
        dmc.Space(h=10),  # no-prism
        dmc.Alert(message, title="Danger!", color="red"),
        dmc.Space(h=10),  # no-prism
        dmc.Alert(message, title="Info", color="violet"),
    ]
)

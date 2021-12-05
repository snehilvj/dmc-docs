import dash_mantine_components as dmc
from dash import html
from utils import create_component_title


alert = html.Div(
    [
        create_component_title("Alerts"),
        dmc.Alert(
            "This alert will disappear in 5 secs",
            title="Auto dismisable alert!",
            color="red",
            duration=5000,
            show=True,
        ),
        dmc.Space(),
        dmc.Alert(
            "Something terrible happened! You made a mistake and there is no going back, your data was lost forever! ",
            title="Bummer!",
            id="alert",
            color="violet",
            withCloseButton=True,
            show=True,
        ),
        dmc.Space(h=20),
        dmc.Button("Toggle alert", id="alert-button"),
        dmc.Space(h=30),
    ]
)

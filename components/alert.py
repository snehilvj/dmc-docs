import dash_mantine_components as dmc
from dash import dcc, html

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
    OnlyCodeBlock,
    OnlyComponentBlock,
    SubText,
    Title,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Alert.__doc__)

message = "Something happened! You made a mistake and there is no going back!"

layout = html.Div(
    children=[
        ComponentName("Alert"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple Alert",
            caption=dcc.Markdown(
                "Create an alert with the main message (`children`), the `title`, and the `color`."
            ),
            code="""import dash_mantine_components as dmc

component = dmc.Alert(
    "Something happened! You made a mistake and there is no going back, your data was lost forever!",
    title="Simple Alert!",
)""",
        ),
        Title("Different colors"),
        SubText(dcc.Markdown("Set the color using `color` argument.")),
        OnlyComponentBlock(
            [
                html.Div(
                    [
                        dmc.Alert(
                            message, title="Primary", color="blue", class_name="alert"
                        ),
                        dmc.Alert(
                            message, title="Secondary", color="gray", class_name="alert"
                        ),
                        dmc.Alert(
                            message, title="Success!", color="green", class_name="alert"
                        ),
                        dmc.Alert(
                            message,
                            title="Warning!",
                            color="yellow",
                            class_name="alert",
                        ),
                        dmc.Alert(
                            message, title="Danger!", color="red", class_name="alert"
                        ),
                        dmc.Alert(message, title="Info", color="violet"),
                    ]
                )
            ]
        ),
        OnlyCodeBlock(
            """import dash_mantine_components as dmc
from dash import html

message = "Something happened! You made a mistake and there is no going back!"

component = html.Div([
    dmc.Alert(message, title="Primary", color="blue"),
    dmc.Alert(message, title="Secondary", color="gray"),
    dmc.Alert(message, title="Success!", color="green"),
    dmc.Alert(message, title="Warning!", color="yellow"),
    dmc.Alert(message, title="Danger!", color="red"),
    dmc.Alert(message, title="Info", color="violet"),
])"""
        ),
        dmc.Space(h=40),
        ComponentBlock(
            title="Dismissable Alerts",
            caption=dcc.Markdown(
                "The alerts can be closed either programmatically by toggling the `hide` property or by clicking on "
                "the close button on the alert if enabled with `withCloseButton=True`. "
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Alert(
        "Something terrible happened! You made a mistake and there is no going back, your data was lost forever! ",
        title="Bummer!",
        id="alert",
        color="red",
        withCloseButton=True,
    ),
    dmc.Space(h=20),
    dmc.Button("Toggle alert", id="alert-button"),
])


@app.callback(
    Output("alert", "hide"),
    Input("alert-button", "n_clicks"),
    State("alert", "hide"),
    prevent_initial_call=True,
)
def alert(n_clicks, hide):
    return not hide""",
        ),
        ComponentBlock(
            title="Automatic Dismissal",
            caption=dcc.Markdown(
                "The alerts can also be timed out using the `duration` prop which accepts time in milliseconds."
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Alert(
        "This alert will dismiss itself after 3 seconds! ",
        title="Auto Dismissing Alert!",
        id="alert-auto",
        color="violet",
        duration=3000
    ),
    dmc.Space(h=20),
    dmc.Button("Show alert", id="alert-auto-button"),
])


@app.callback(
    Output("alert-auto", "hide"),
    Input("alert-auto-button", "n_clicks"),
    prevent_initial_call=True,
)
def alert_auto(n_clicks):
    return False""",
        ),
        ComponentReference(apidocs),
    ]
)

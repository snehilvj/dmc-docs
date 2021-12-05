import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

modal = html.Div(
    [
        create_component_title("Modal"),
        dmc.Button("Open Modal", id="modal-button"),
        dmc.Modal(
            [
                dmc.Text("I am in a modal component."),
                dmc.Space(h=20),
                dmc.Group(
                    [
                        dmc.Button("Submit", id="modal-submit-button"),
                        dmc.Button(
                            "Close",
                            color="red",
                            variant="outline",
                            id="modal-close-button",
                        ),
                    ],
                    position="right",
                ),
            ],
            title="New Modal",
            id="modal",
        ),
        dmc.Space(h=30),
    ]
)

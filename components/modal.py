import dash_mantine_components as dmc
from dash import html

title = "Modal"
doc = dmc.Modal.__doc__

layout = html.Div(
    children=[
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
            id="modal-demo",
        ),
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.Group(
            [
                dmc.Button("Open Modal", id="modal-demo-button"),
                dmc.Switch(label="Centered", id="centered-modal-demo"),
            ]
        ),
        dmc.Space(h=50),
        dmc.Text("Sizes", color="dimmed"),
        dmc.Space(h=10),
        dmc.Modal(id="modal-size-demo", children=[dmc.Space(h=200)]),
        dmc.Group(
            children=[
                dmc.Button(label, id=f"{label}-button-modal", variant="outline")
                for label in ["lg", "378px", "55%", "full"]
            ]
        ),
    ]
)

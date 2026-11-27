from dash import html, callback, Input, Output, State
import dash_mantine_components as dmc

slides = [
    {"src": f"https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-{i}.png"}
    for i in range(1, 6)
]

component = dmc.Box([
    dmc.Lightbox(
        id="lightbox-oc-transition",
        opened=False,
        slides=slides,
        transitionProps={"transition": "pop", "duration": 400},
    ),
    dmc.Group([
        dmc.Select(
            label="Transition",
            data=["fade", "pop", "scale", "slide-up", "slide-down", "rotate-left"],
            value="slide-up",
            id="lightbox-oc-transition-sel",
            allowDeselect=False,
        ),
        dmc.Button("Open lightbox", id="open-lightbox-oc-transition"),
    ], align="flex-end"),
])



@callback(
    Output("lightbox-oc-transition", "opened"),
    Input("open-lightbox-oc-transition", "n_clicks"),
    prevent_initial_call=True,
)
def open_lightbox(n):
    return True


@callback(
    Output("lightbox-oc-transition", "transitionProps"),
    Input("lightbox-oc-transition-sel", "value"),
)
def update_transition(transition):
    return {"transition": transition, "duration": 400}
import dash_mantine_components as dmc
from dash import callback, Input, Output, ctx


lorem = (
    "Lorem ipsum, dolor sit amet consectetur adipisicing elit. "
    "Dicta perspiciatis reiciendis voluptate eaque itaque quos. "
    "Natus iure tenetur libero, reprehenderit ad, sequi, in aliquam eos "
    "necessitatibus expedita delectus veniam culpa!"
)

component = dmc.Box([
    dmc.Group([
        dmc.Button("Scroll to bottom", id="scroll-bottom"),
        dmc.Button("Scroll to middle", id="scroll-middle"),
        dmc.Button("Scroll to top", id="scroll-top"),
    ], mb="lg"),
    dmc.ScrollArea(
        id="scrollArea-buttons",
        h=250, w=350,
        children=[
            dmc.Box(
                w=600,
                children=[
                    dmc.Title(f"Section {i}", order=3, mt="lg", id=f"section-{i}"),
                    dmc.Text(lorem)
                ]
            )
            for i in range(10)
        ]
    ),

])


@callback(
    Output("scrollArea-buttons", "scrollTo"),
    Input("scroll-top", "n_clicks"),
    Input("scroll-middle", "n_clicks"),
    Input("scroll-bottom", "n_clicks"),
)
def scroll_to(t, m, b):
    if ctx.triggered_id == "scroll-bottom":
        return {"top": 100}
    if ctx.triggered_id == "scroll-middle":
        return {"top": 50}
    return {"top": 0}


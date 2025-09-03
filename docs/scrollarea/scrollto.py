import dash_mantine_components as dmc
from dash import callback, Input, Output


lorem = (
    "Lorem ipsum, dolor sit amet consectetur adipisicing elit. "
    "Dicta perspiciatis reiciendis voluptate eaque itaque quos. "
    "Natus iure tenetur libero, reprehenderit ad, sequi, in aliquam eos "
    "necessitatibus expedita delectus veniam culpa!"
)

component = dmc.Box([
    dmc.Group([
        dmc.NumberInput(label="Scroll to vertical position (0-100)%", min=0, max=100, value=0, id="y-position"),
        dmc.NumberInput(label="Scroll to horizontal position (0-100)%", min=0, max=100, value=0, id="x-position"),
    ], mb="lg"),
    dmc.ScrollArea(
        id="scrollArea",
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
    Output("scrollArea", "scrollTo"),
    Input("x-position", "value"),
    Input("y-position", "value")
)
def scroll_to(x, y):
    return {"top": y, "left": x}


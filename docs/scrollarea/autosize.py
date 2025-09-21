
import dash_mantine_components as dmc
from dash import callback, Output, Input, ctx

lorem = (
    "Lorem ipsum, dolor sit amet consectetur adipisicing elit. "
    "Dicta perspiciatis reiciendis voluptate eaque itaque quos. "
    "Natus iure tenetur libero, reprehenderit ad, sequi, in aliquam eos "
    "necessitatibus expedita delectus veniam culpa!"
)

component = dmc.Stack(
    [
        dmc.ScrollAreaAutosize(mah=300, maw=400, p="sm", id="scrollarea-autosize"),
        dmc.Group(
            m="lg",
            children=[
                dmc.Button(
                    "1 paragraph",
                    id="btn-1-paragraph",
                    color="red",
                ),
                dmc.Button(
                    "4 paragraphs",
                    id="btn-4-paragraphs",
                ),
            ],
        ),
    ]
)


@callback(
    Output("scrollarea-autosize", "children"),
    Input("btn-1-paragraph", "n_clicks"),
    Input("btn-4-paragraphs", "n_clicks"),
)
def update_paragraphs(inc, dec):
    if ctx.triggered_id == "btn-1-paragraph":
        return dmc.Box(lorem, p="sm")
    return [dmc.Box(lorem, p="sm") for _ in range(4)]

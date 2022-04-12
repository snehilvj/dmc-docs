import dash_mantine_components as dmc
from dash import Output, Input, html
from dash import callback

component = html.Div(
    children=[
        dmc.Accordion(
            id="accordion",
            state={"0": False, "1": True},
            children=[
                dmc.AccordionItem(
                    "Content 1",
                    label="Section 1",
                ),
                dmc.AccordionItem(
                    "Content 2",
                    label="Section 2",
                ),
            ],
        ),
        dmc.Text(id="accordion-state", style={"marginTop": 10}),
    ]
)


@callback(Output("accordion-state", "children"), Input("accordion", "state"))
def show_state(state):
    return str(state)

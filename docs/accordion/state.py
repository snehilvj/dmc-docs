import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    children=[
        dmc.Accordion(
            id="accordion-simple",
            value="customization",
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Customization"),
                        dmc.AccordionPanel(
                            "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                        ),
                    ],
                    value="customization",
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Flexibility"),
                        dmc.AccordionPanel(
                            "Configure temp appearance and behavior with vast amount of settings or overwrite any "
                            "part of component styles "
                        ),
                    ],
                    value="flexibility",
                ),
            ],
        ),
        dmc.Text(id="accordion-state", mt=10),
    ]
)


@callback(Output("accordion-state", "children"), Input("accordion-simple", "value"))
def show_state(value):
    return value

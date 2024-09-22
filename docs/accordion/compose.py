import dash_mantine_components as dmc
from dash import Output, Input, html, callback, MATCH
from dash_iconify import DashIconify


def make_control(text, action_id):
    return dmc.Flex(
        [
            dmc.AccordionControl(text),
            dmc.ActionIcon(
                children=DashIconify(icon="tabler:heart"),
                color="yellow",
                variant="default",
                n_clicks=0,
                id={"index": action_id},
            ),
        ],
        justify="space-between",
    )


component = dmc.Accordion(
    id="accordion-compose-controls",
    chevronPosition="left",
    children=[
        dmc.AccordionItem(
            [
                make_control(f"Item {i}", f"action-{i}"),
                dmc.AccordionPanel(f"Content for AccordionItem {i}"),
            ],
            value=f"item-{i}",
        )
        for i in range(5)
    ],
)


@callback(Output({"index": MATCH}, "variant"), Input({"index": MATCH}, "n_clicks"))
def update_heart(n):
    if n % 2 == 0:
        return "default"
    return "filled"

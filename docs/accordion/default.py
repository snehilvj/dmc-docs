import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Accordion(
    icon=[DashIconify(icon="tabler:arrow-big-down-line")],
    children=[
        dmc.AccordionItem(
            label="Customization",
        ),
        dmc.AccordionItem(
            label="Flexibility",
        ),
        dmc.AccordionItem(
            label="No annoying focus ring",
        ),
    ],
)

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Accordion(
    disableIconRotation=True,
    children=[
        dmc.AccordionItem(
            label="Personal Information",
            icon=[
                DashIconify(
                    icon="tabler:user",
                    color=dmc.theme.DEFAULT_COLORS["blue"][6],
                    width=20,
                )
            ],
        ),
        dmc.AccordionItem(
            label="Shipping Address",
            icon=[
                DashIconify(
                    icon="tabler:map-pin",
                    color=dmc.theme.DEFAULT_COLORS["red"][6],
                    width=20,
                )
            ],
        ),
        dmc.AccordionItem(
            label="Confirmation",
            icon=[
                DashIconify(
                    icon="tabler:circle-check",
                    color=dmc.theme.DEFAULT_COLORS["green"][6],
                    width=20,
                )
            ],
        ),
    ],
)

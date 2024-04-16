import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Accordion(
    disableChevronRotation=True,
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Personal Information",
                    icon=DashIconify(
                        icon="tabler:user",
                        color=dmc.DEFAULT_THEME["colors"]["blue"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("some content"),
            ],
            value="info",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Shipping Address",
                    icon=DashIconify(
                        icon="tabler:map-pin",
                        color=dmc.DEFAULT_THEME["colors"]["red"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("some content"),
            ],
            value="addr",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Confirmation",
                    icon=DashIconify(
                        icon="tabler:circle-check",
                        color=dmc.DEFAULT_THEME["colors"]["green"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("some content"),
            ],
            value="focus",
        ),
    ],
)

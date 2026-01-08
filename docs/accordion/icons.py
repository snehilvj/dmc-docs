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
                        color="var(--mantine-color-blue-6)",
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
                        color= "var(--mantine-color-red-6)",
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
                        color= "var(--mantine-color-green-6)",
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("some content"),
            ],
            value="focus",
        ),
    ],
)

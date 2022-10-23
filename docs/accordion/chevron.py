import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Accordion(
    chevron=DashIconify(icon="ant-design:plus-outlined"),
    disableChevronRotation=True,
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
                    "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                    "component styles "
                ),
            ],
            value="flexibility",
        ),
    ],
)

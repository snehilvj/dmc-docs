import dash_mantine_components as dmc

component = dmc.Accordion(
    children=[
        dmc.AccordionItem(
            "Colors, fonts, shadows and many other parts are customizable to fit your design needs",
            label="Customization",
        ),
        dmc.AccordionItem(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of component "
            "styles",
            label="Flexibility",
        ),
    ],
)

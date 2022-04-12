import dash_mantine_components as dmc

component = dmc.Accordion(
    multiple=True,
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
)

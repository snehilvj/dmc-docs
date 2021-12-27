import dash_mantine_components as dmc

title = "Accordion"
doc = dmc.Accordion.__doc__

layout = dmc.Accordion(
    children=[
        dmc.AccordionItem(
            "Colors, fonts, shadows and many other parts are customizable to fit your design needs",
            label="Customization",
        ),
        dmc.AccordionItem(
            "Configure components appearance and behavior with vast amount of settings or overwrite any part of component styles",
            label="Flexibility",
        ),
        dmc.AccordionItem(
            "With new :focus-visible pseudo-class focus ring appears only when user navigates with keyboard",
            label="No annoying focus ring",
        ),
    ],
)

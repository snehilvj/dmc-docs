import dash_mantine_components as dmc
from dash import html

title = "Accordion"
doc = dmc.Accordion.__doc__

layout = html.Div(
    children=[
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.Accordion(
            children=[
                dmc.AccordionItem(
                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs",
                    label="Customization",
                ),
                dmc.AccordionItem(
                    "Configure components appearance and behavior with vast amount of settings or overwrite any part of component styles",
                    label="Flexibility",
                ),
            ],
        ),
        dmc.Space(h=50),
        dmc.Text("With description", color="dimmed"),
        dmc.Space(h=10),
        dmc.Accordion(
            children=[
                dmc.AccordionItem(
                    "Configure components appearance and behavior with vast amount of settings or overwrite any part of component styles",
                    label="Flexibility",
                    description="Description about flexibility",
                ),
                dmc.AccordionItem(
                    "With new :focus-visible pseudo-class focus ring appears only when user navigates with keyboard",
                    label="No annoying focus ring",
                    description="Something something about something",
                ),
            ],
        ),
    ]
)

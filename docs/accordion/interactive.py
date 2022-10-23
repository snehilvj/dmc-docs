import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "chevronPosition",
        "component": "DemoSegmentedControl",
        "data": ["left", "right"],
        "value": "left",
    },
    {
        "property": "variant",
        "component": "Select",
        "data": ["default", "contained", "filled", "separated"],
        "value": "default",
    },
    {
        "property": "disableChevronRotation",
        "component": "Switch",
        "checked": False,
    },
    {
        "property": "radius",
        "component": "DemoSlider",
        "value": "sm",
    },
]

demo = dmc.Accordion(
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
        dmc.AccordionItem(
            [
                dmc.AccordionControl("No annoying focus ring"),
                dmc.AccordionPanel(
                    "With new :focus-visible pseudo-class focus ring appears only when user navigates with keyboard"
                ),
            ],
            value="focus",
        ),
    ],
)

component = create_configurator(demo, controls, center=False)

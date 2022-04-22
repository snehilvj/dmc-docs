import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "iconPosition",
        "component": "SegmentedControl",
        "data": ["left", "right"],
        "value": "left",
    },
    {"property": "offsetIcon", "component": "Switch", "checked": True},
    {
        "property": "disableIconRotation",
        "component": "Switch",
        "checked": False,
    },
    {"property": "multiple", "component": "Switch", "checked": False},
]

demo = dmc.Accordion(
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
        dmc.AccordionItem(
            "With new :focus-visible pseudo-class focus ring appears only when user navigates with keyboard",
            label="No annoying focus ring",
        ),
    ],
)

component = create_configurator(demo, controls, center=False)

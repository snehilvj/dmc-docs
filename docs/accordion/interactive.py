import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Accordion(
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

configurator = Configurator(target)

configurator.add_segmented_control("chevronPosition", ["left", "right"], "left")
configurator.add_select(
    "variant", ["default", "contained", "filled", "separated"], "separated"
)
configurator.add_switch("disableChevronRotation", False)
configurator.add_slider("radius", "sm")

component = configurator.panel

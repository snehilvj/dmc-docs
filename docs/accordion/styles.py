import dash_mantine_components as dmc

component = dmc.Accordion(
    value="flexibility",
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
                dmc.AccordionControl("No Annoying Focus Ring"),
                dmc.AccordionPanel(
                    "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                    "component styles "
                ),
            ],
            value="ring",
        ),
    ],
    styles={
        "root": {"borderRadius": 5},
        "item": {
            "border": "1px solid transparent",
            "position": "relative",
            "zIndex": 0,
            "transition": "transform 150ms ease",
            "&[data-active]": {
                "transform": "scale(1.03)",
                "boxShadow": 5,
                "borderColor": dmc.theme.DEFAULT_COLORS["gray"][6],
                "borderRadius": 5,
                "zIndex": 1,
            },
        },
        "chevron": {
            "&[data-rotate]": {"transform": "rotate(-90deg)"},
        },
    },
)

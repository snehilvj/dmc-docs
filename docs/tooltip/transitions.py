import dash_mantine_components as dmc

component = dmc.Group(
    position="center",
    children=[
        dmc.Tooltip(
            children=[dmc.Badge(transition)],
            transitionProps={"transition": transition, "duration": 300},
            label=transition,
        )
        for transition in [
            "fade",
            "skew-up",
            "skew-down",
            "rotate-right",
            "rotate-left",
            "slide-down",
            "slide-up",
            "slide-right",
            "slide-left",
            "scale-y",
            "scale-x",
            "scale",
            "pop",
            "pop-top-left",
            "pop-top-right",
            "pop-bottom-left",
            "pop-bottom-right",
        ]
    ],
)

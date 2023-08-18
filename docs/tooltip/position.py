import dash_mantine_components as dmc

component = dmc.Group(
    position="center",
    children=[
        dmc.Tooltip(
            children=[dmc.Button(position, variant="outline")],
            withArrow=True,
            label=position,
            position=position,
        )
        for position in [
            "top",
            "right",
            "bottom",
            "left",
            "top-end",
            "top-start",
            "right-end",
            "right-start",
            "bottom-end",
            "bottom-start",
            "left-end",
            "left-start",
        ]
    ],
)

import dash_mantine_components as dmc

component = dmc.Group(
    position="center",
    children=[
        dmc.Tooltip(
            children=[dmc.Button(f"{position}-{placement}", variant="outline")],
            withArrow=True,
            label=f"{position}-{placement}",
            position=position,
            placement=placement,
        )
        for position in [
            "top",
            "bottom",
            "right",
            "left",
        ]
        for placement in ["start", "center", "end"]
    ],
)

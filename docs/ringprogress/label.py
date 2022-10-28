import dash_mantine_components as dmc

component = (
    dmc.RingProgress(
        id="ring-progress",
        sections=[{"value": 33, "color": "indigo"}],
        label=dmc.Center(dmc.Text("33%", color="indigo")),
    ),
)


import dash_mantine_components as dmc

component = dmc.Group([
    dmc.Progress(value=80, orientation="vertical", h=200),

    dmc.Progress(
        value=60,
        color="orange",
        size="xl",
        orientation="vertical",
        h=200,
        animated=True
    ),

    dmc.ProgressRoot(
        size="xl",
        autoContrast=True,
        orientation="vertical",
        h=200,
        children=[
            dmc.ProgressSection(
                value=40,
                color="lime.4",
                children=dmc.ProgressLabel("Documents")
            ),
            dmc.ProgressSection(
                value=20,
                color="yellow.4",
                children=dmc.ProgressLabel("Apps")
            ),
            dmc.ProgressSection(
                value=20,
                color="cyan.7",
                children=dmc.ProgressLabel("Other")
            )
        ]
    )
])

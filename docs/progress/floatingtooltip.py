import dash_mantine_components as dmc

component = dmc.ProgressRoot(
    [
        dmc.FloatingTooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Documents"),
                value=33,
                color="cyan",
            ),
            label="Documents – 33Gb",
            boxWrapperProps={"display": "contents"},
        ),
        dmc.FloatingTooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Photos"),
                value=28,
                color="pink",
            ),
            label="Photos – 28Gb",
            boxWrapperProps={"display": "contents"},
        ),
        dmc.FloatingTooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Other"),
                value=25,
                color="orange",
            ),
            label="Other – 15Gb",
            boxWrapperProps={"display": "contents"},
        ),
    ],
    size=40,
)

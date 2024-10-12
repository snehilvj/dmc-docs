import dash_mantine_components as dmc

component = dmc.ProgressRoot(
    [
        dmc.Tooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Documents"), value=33, color="cyan", w="100%"
            ),
            label="Documents – 33Gb",
            boxWrapperProps={"w": "33%"},
        ),
        dmc.Tooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Photos"), value=28, color="pink", w="100%"
            ),
            label="Photos – 28Gb",
            boxWrapperProps={"w": "28%"},
        ),
        dmc.Tooltip(
            dmc.ProgressSection(
                dmc.ProgressLabel("Other"), value=25, color="orange", w="100%"
            ),
            label="Other – 15Gb",
            boxWrapperProps={"w": "25%"},
        ),
    ],
    size=40,
)

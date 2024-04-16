import dash_mantine_components as dmc

component = dmc.ProgressRoot(
    [
        dmc.Tooltip(
            dmc.ProgressSection(dmc.ProgressLabel("Documents"), value=33, color="cyan"),
            label="Documents – 33GB",
        ),
        dmc.Tooltip(
            dmc.ProgressSection(dmc.ProgressLabel("Photos"), value=28, color="pink"),
            label="Photos – 28GB",
        ),
        dmc.Tooltip(
            dmc.ProgressSection(dmc.ProgressLabel("Others"), value=15, color="orange"),
            label="Others – 15GB",
        ),
    ],
    size="xl",
)

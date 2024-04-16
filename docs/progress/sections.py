import dash_mantine_components as dmc

component = dmc.ProgressRoot(
    [
        dmc.ProgressSection(dmc.ProgressLabel("Documents"), value=33, color="cyan"),
        dmc.ProgressSection(dmc.ProgressLabel("Photos"), value=28, color="pink"),
        dmc.ProgressSection(dmc.ProgressLabel("Others"), value=15, color="orange"),
    ],
    size="xl",
)

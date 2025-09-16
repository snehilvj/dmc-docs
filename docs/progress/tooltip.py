import dash_mantine_components as dmc


component = dmc.Box(
    [
        dmc.ProgressRoot(
            [
                dmc.ProgressSection(
                    dmc.ProgressLabel("Documents"),
                    value=33,
                    color="cyan",
                    id="progress-section1",
                ),
                dmc.ProgressSection(
                    dmc.ProgressLabel("Photos"),
                    value=28,
                    color="pink",
                    id="progress-section2",
                ),
                dmc.ProgressSection(
                    dmc.ProgressLabel("Others"),
                    value=15,
                    color="orange",
                    id="progress-section3",
                ),
            ],
            size="40",
        ),
        dmc.Tooltip(
            target="#progress-section1",
            label="Documents – 33Gb",
        ),
        dmc.Tooltip(
            target="#progress-section2",
            label="Photos – 28Gb",
        ),
        dmc.Tooltip(
            target="#progress-section3",
            label="Other – 15Gb",
        ),
    ]
)



import dash_mantine_components as dmc

sections = [
    {"value": 40, "color": "cyan"},
    {"value": 25, "color": "orange"},
    {"value": 15, "color": "grape"},
]

component = dmc.Stack(
    [
        dmc.Box(
            [
                dmc.Text("No gap (default)", size="sm", ta="center", mb="xs"),
                dmc.RingProgress(sections=sections),
            ]
        ),
        dmc.Box(
            [
                dmc.Text("5° gap", size="sm", ta="center", mb="xs"),
                dmc.RingProgress(sections=sections, sectionGap=5),
            ]
        ),
        dmc.Box(
            [
                dmc.Text("10° gap", size="sm", ta="center", mb="xs"),
                dmc.RingProgress(sections=sections, sectionGap=10),
            ]
        ),
    ],
    align="center",
)


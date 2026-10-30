
import dash_mantine_components as dmc

sections = [{"value": 40, "color": "cyan"}]

component = dmc.Group(
    [
        dmc.Stack(
            [
                dmc.RingProgress(sections=sections, startAngle=0),
                dmc.Text("0° (right)", size="sm"),
            ],
            align="center",
            gap="xs",
        ),
        dmc.Stack(
            [
                dmc.RingProgress(sections=sections, startAngle=90),
                dmc.Text("90° (bottom)", size="sm"),
            ],
            align="center",
            gap="xs",
        ),
        dmc.Stack(
            [
                dmc.RingProgress(sections=sections, startAngle=180),
                dmc.Text("180° (left)", size="sm"),
            ],
            align="center",
            gap="xs",
        ),
        dmc.Stack(
            [
                dmc.RingProgress(sections=sections, startAngle=270),
                dmc.Text("270° (top)", size="sm"),
            ],
            align="center",
            gap="xs",
        ),
    ],
    justify="center",
)


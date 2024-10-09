import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Group(
            [
                dmc.Chip("Outline default", variant="outline", controlled=True),
                dmc.Chip(
                    "Outline checked", variant="outline", controlled=True, checked=True
                ),
                dmc.Chip("Outline disabled", variant="outline", controlled=True),
            ]
        ),
        dmc.Group(
            [
                dmc.Chip("Light default", variant="light", controlled=True, m="sm"),
                dmc.Chip(
                    "Light checked",
                    variant="light",
                    controlled=True,
                    checked=True,
                    m="sm",
                ),
                dmc.Chip("Light disabled", variant="light", controlled=True, m="sm"),
            ]
        ),
        dmc.Group(
            [
                dmc.Chip("Filled default", variant="filled", controlled=True, m="sm"),
                dmc.Chip(
                    "Filled checked",
                    variant="filled",
                    controlled=True,
                    checked=True,
                    m="sm",
                ),
                dmc.Chip("Filled disabled", variant="filled", controlled=True, m="sm"),
            ]
        ),
    ],
)

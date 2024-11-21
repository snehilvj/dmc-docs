import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Group(
            [
                dmc.Chip("Outline default", variant="outline"),
                dmc.Chip(
                    "Outline checked", variant="outline", checked=True
                ),
                dmc.Chip("Outline disabled", disabled=True, variant="outline"),
            ]
        ),
        dmc.Group(
            [
                dmc.Chip("Light default", variant="light",  m="sm"),
                dmc.Chip(
                    "Light checked",
                    variant="light",
                    checked=True,
                    m="sm",
                ),
                dmc.Chip("Light disabled", disabled=True, variant="light", m="sm"),
            ]
        ),
        dmc.Group(
            [
                dmc.Chip("Filled default", variant="filled", m="sm"),
                dmc.Chip(
                    "Filled checked",
                    variant="filled",
                    checked=True,
                    m="sm",
                ),
                dmc.Chip("Filled disabled", disabled=True, variant="filled", m="sm"),
            ]
        ),
    ],
)

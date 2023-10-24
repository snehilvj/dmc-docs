import dash_mantine_components as dmc


component = dmc.Stack(
    [
        dmc.Group(
            [
                dmc.Text("Fractions: 2"),
                dmc.Rating(fractions=2, defaultValue=2, value=1)
            ]
        ),
        dmc.Group(
            [
                dmc.Text("Fractions: 3"),
                dmc.Rating(fractions=3, defaultValue=2, value=2.3333)
            ]
        ),
        dmc.Group(
            [
                dmc.Text("Fractions: 4"),
                dmc.Rating(fractions=4, defaultValue=2, value=3.75)
            ]
        )
    ]
)
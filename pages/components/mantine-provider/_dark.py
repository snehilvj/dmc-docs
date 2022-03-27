from datetime import date

import dash_mantine_components as dmc

component = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    children=[
        dmc.Paper(
            [
                dmc.Group(
                    grow=True,
                    direction="column",
                    children=[
                        dmc.DatePicker(
                            style={"width": 200},
                            label="Select Date",
                            value=date.today(),
                        ),
                        dmc.Alert("This is an alert!", title="An Alert", color="red"),
                    ],
                )
            ],
            p="md",
        )
    ],
)

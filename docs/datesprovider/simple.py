import dash_mantine_components as dmc

component = dmc.DatesProvider(
    children=dmc.Stack(
        [
            dmc.DatePicker(
                w=250,
                label="Sélectionner une date",
            ),
            dmc.DatePicker(
                w=250,
                label="Sélectionner une autre date",
            ),
        ]
    ),
    settings={"locale": "fr", "firstDayOfWeek": 0, "weekendDays": [0]},
)

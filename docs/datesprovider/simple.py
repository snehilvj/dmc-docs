import dash_mantine_components as dmc

component = dmc.DatesProvider(
    children=[
        dmc.DatePickerInput(
            id="fr-date-picker-input",
            style={"width": 200},
            label="Sélectionner une date"
        ),
        dmc.DatePickerInput(
            id="fr-date-picker-input-2",
            style={"width": 200},
            label="Sélectionner une autre date"
        ),
    ],
    settings={"locale": "fr", "firstDayOfWeek": 0, "weekendDays": [0]}
)



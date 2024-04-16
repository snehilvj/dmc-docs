import dash_mantine_components as dmc

component = dmc.DatesProvider(
    dmc.DatePicker(
        id="fr-date-picker-input", style={"width": 200}, label="Sélectionner une date"
    ),
    settings={"locale": "fr"},
)

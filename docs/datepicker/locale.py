import dash_mantine_components as dmc

component = dmc.DatesProvider(
    dmc.DatePicker(
        id="fr-date-picker",
        style={"width": 200},
    ),
    settings={"locale": "fr"}
)

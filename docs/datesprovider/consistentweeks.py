import dash_mantine_components as dmc

component = dmc.DatesProvider(
    children=dmc.DatePickerInput(
                h=400,
                popoverProps={
                    "opened": True,
                    "position": "bottom",
                    "middlewares":{ "flip": False, "shift": False }
                }
            ),
    settings={"consistentWeeks": True},
)

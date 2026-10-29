from datetime import date

import dash_mantine_components as dmc

this_year = date.today().year
start_of_year = lambda year: date(year, 1, 1).isoformat()

component = dmc.YearPickerInput(
    type="range",
    label="With presets",
    placeholder="Select years range",
    presets=[
        {
            "value": [start_of_year(this_year - 2), start_of_year(this_year)],
            "label": "Last 2 years",
        },
        {
            "value": [start_of_year(this_year - 5), start_of_year(this_year)],
            "label": "Last 5 years",
        },
        {
            "value": [start_of_year(this_year), start_of_year(this_year + 5)],
            "label": "Next 5 years",
        },
        {
            "value": [start_of_year(this_year - 10), start_of_year(this_year)],
            "label": "Last decade",
        },
    ],
)
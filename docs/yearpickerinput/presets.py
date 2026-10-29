from datetime import date

import dash_mantine_components as dmc

this_year = date.today().year

component = dmc.YearPickerInput(
    label="With presets",
    placeholder="Select year",
    presets=[
        {"value": date(this_year, 1, 1).isoformat(), "label": "This year"},
        {"value": date(this_year + 1, 1, 1).isoformat(), "label": "Next year"},
        {"value": date(this_year - 1, 1, 1).isoformat(), "label": "Last year"},
        {"value": date(this_year + 5, 1, 1).isoformat(), "label": "In 5 years"},
        {"value": date(this_year - 5, 1, 1).isoformat(), "label": "5 years ago"},
    ],
)

from datetime import date

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Stack([
    dmc.YearPickerInput(
        label="clearSectionMode='both' (default)",
        placeholder="Pick date",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="both",
    ),
    dmc.YearPickerInput(
        label="clearSectionMode='rightSection'",
        placeholder="Pick date",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="rightSection",
    ),
    dmc.YearPickerInput(
        label="clearSectionMode='clear'",
        placeholder="Pick date",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="clear",
    ),
])


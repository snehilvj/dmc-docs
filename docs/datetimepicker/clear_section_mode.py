
from datetime import date

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Stack([
    dmc.DateTimePicker(
        label="clearSectionMode='both' (default)",
        placeholder="Pick a date and time",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="both",
    ),
    dmc.DateTimePicker(
        label="clearSectionMode='rightSection'",
        placeholder="Pick a date and time",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="rightSection",
    ),
    dmc.DateTimePicker(
        label="clearSectionMode='clear'",
        placeholder="Pick a date and time",
        value="2027-01-01",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="clear",
    ),
])


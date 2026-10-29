
from datetime import date

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Stack([
    dmc.TimePicker(
        label="clearSectionMode='both' (default)",
        placeholder="Pick time",
        value="12:30",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="both",
    ),
    dmc.TimePicker(
        label="clearSectionMode='rightSection'",
        placeholder="Pick time",
        value="12:30",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="rightSection",
    ),
    dmc.TimePicker(
        label="clearSectionMode='clear'",
        placeholder="Pick time",
        value="12:30",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="clear",
    ),
])


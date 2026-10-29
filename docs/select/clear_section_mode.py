
import dash_mantine_components as dmc
from dash_iconify import DashIconify

data = ["Mercury", "Venus", "Earth", "Mars"]

component = dmc.Stack([
    dmc.Select(
        label="clearSectionMode='both' (default)",
        placeholder="Pick a planet",
        data=data,
        value="Earth",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="both",
    ),
    dmc.Select(
        label="clearSectionMode='rightSection'",
        placeholder="Pick a planet",
        data=data,
        value="Earth",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="rightSection",
    ),
    dmc.Select(
        label="clearSectionMode='clear'",
        placeholder="Pick a planet",
        data=data,
        value="Earth",
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="clear",
    ),
])



import dash_mantine_components as dmc
from dash_iconify import DashIconify

data = [f"Option-{i}" for i in range(6)]

component = dmc.Stack([
    dmc.MultiSelect(
        label="clearSectionMode='both' (default)",
        placeholder="Select options",
        data=data,
        value=["Option-1", "Option-2"],
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="both",
    ),
    dmc.MultiSelect(
        label="clearSectionMode='rightSection'",
        placeholder="Select options",
        data=data,
        value=["Option-1", "Option-2"],
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="rightSection",
    ),
    dmc.MultiSelect(
        label="clearSectionMode='clear'",
        placeholder="Select options",
        data=data,
        value=["Option-1", "Option-2"],
        clearable=True,
        rightSection=DashIconify(icon="tabler:chevron-down", width=16),
        clearSectionMode="clear",
    ),
])


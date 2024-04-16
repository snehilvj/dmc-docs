import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    children=[
        dmc.Avatar(
            src="https://avatars.githubusercontent.com/u/91216500?v=4", radius="xl"
        ),
        # default placeholder
        dmc.Avatar(radius="xl"),
        # initials
        dmc.Avatar("MK", color="cyan", radius="xl"),
        # icon
        dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue", radius="xl"),
    ],
)

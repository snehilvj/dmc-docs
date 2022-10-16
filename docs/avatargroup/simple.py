import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.AvatarGroup(
    children=[
        dmc.Avatar(src="https://avatars.githubusercontent.com/u/91216500?v=4"),
        dmc.Avatar(),
        dmc.Avatar("MK", color="cyan"),
        dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue"),
    ],
    limit=3,
)

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.AvatarGroup(
    children=[
        dmc.Avatar(
            src="https://avatars.githubusercontent.com/u/91216500?v=4", radius="xl"
        ),
        dmc.Avatar(
            src="https://avatars.githubusercontent.com/u/24227892?v=4", radius="xl"
        ),
        dmc.Avatar(radius="xl"),
        dmc.Avatar("MK", color="cyan", radius="xl"),
        dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue", radius="xl"),
    ],
)

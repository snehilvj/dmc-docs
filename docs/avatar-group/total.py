import dash_mantine_components as dmc

component = dmc.AvatarGroup(
    total=7,
    limit=2,
    size="lg",
    children=[
        dmc.Avatar(src="https://avatars.githubusercontent.com/u/91216500?v=4"),
        dmc.Avatar(src="https://avatars.githubusercontent.com/u/24227892?v=4"),
    ],
)

import dash_mantine_components as dmc

component = dmc.Badge(
    "Badge with Avatar",
    leftSection=dmc.Avatar(
        src="https://avatars.githubusercontent.com/u/91216500?v=4",
        size=24,
        radius="xl",
        mr=5,
    ),
    sx={"paddingLeft": 0},
    size="lg",
    radius="xl",
    color="teal",
)

import dash_mantine_components as dmc

component = dmc.Indicator(
    dmc.Avatar(
        size="lg",
        radius="sm",
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
    ),
    inline=True,
    size=16,
    label="New",
)

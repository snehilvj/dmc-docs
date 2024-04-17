import dash_mantine_components as dmc

component = dmc.Indicator(
    dmc.Avatar(
        size="lg",
        radius="xl",
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
    ),
    inline=True,
    offset=7,
    position="bottom-end",
    color="red",
    withBorder=True,
    size=16,
)

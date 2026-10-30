import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Indicator(
            dmc.Avatar(
                size="lg",
                radius="xl",
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
            ),
            inline=True,
            label=50,
            maxValue=99,
        ),
        dmc.Indicator(
            dmc.Avatar(
                size="lg",
                radius="xl",
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
            ),
            inline=True,
            label=100,
            maxValue=99,
        ),
        dmc.Indicator(
            dmc.Avatar(
                size="lg",
                radius="xl",
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
            ),
            inline=True,
            label=1000,
            maxValue=999,
        ),
    ]
)


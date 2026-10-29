
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
            label="99",
            color="lime.4",
        ),
        dmc.Indicator(
            dmc.Avatar(
                size="lg",
                radius="xl",
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
            ),
            inline=True,
            label="99",
            color="lime.4",
            autoContrast=True,
        ),
    ]
)

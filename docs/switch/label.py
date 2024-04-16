import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Switch(onLabel="ON", offLabel="OFF", radius="xl", size=x)
        for x in ["xs", "sm", "md", "lg", "xl"]
    ]
)

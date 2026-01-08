import dash_mantine_components as dmc
from dash_iconify import DashIconify

icons = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:moon", width=20),
    onLabel=DashIconify(icon="radix-icons:sun", width=20),
    size="xl", color="yellow"
)


thumbicon = dmc.Switch(
    thumbIcon=DashIconify(
        icon="tabler:walk", width=16, color= "var(--mantine-color-teal-5)"
    ),
    size="lg",
    color="teal",
    checked=True,
)


default = dmc.Switch()


label = dmc.Group(
    [
        dmc.Switch(onLabel="ON", offLabel="OFF", radius="xl", size="md"),
        dmc.Switch(onLabel="ON", offLabel="OFF", radius="xl", size="lg", checked=True)
    ]
)

component = dmc.Stack([default, label, thumbicon, icons])

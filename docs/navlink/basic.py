import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


component = html.Div(
    [
        dmc.NavLink(
            label="With icon",
            leftSection=get_icon(icon="bi:house-door-fill"),
        ),
        dmc.NavLink(
            label="With right section",
            leftSection=get_icon(icon="tabler:gauge"),
            rightSection=get_icon(icon="tabler-chevron-right"),
        ),
        dmc.NavLink(
            label="Disabled",
            leftSection=get_icon(icon="tabler:circle-off"),
            disabled=True,
        ),
        dmc.NavLink(
            label="With description",
            description="Additional information",
            leftSection=dmc.Badge(
                "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
            ),
        ),
        dmc.NavLink(
            label="Active subtle",
            leftSection=get_icon(icon="tabler:activity"),
            rightSection=get_icon(icon="tabler-chevron-right"),
            variant="subtle",
            active=True,
        ),
        dmc.NavLink(
            label="Active light",
            leftSection=get_icon(icon="tabler:activity"),
            rightSection=get_icon(icon="tabler-chevron-right"),
            active=True,
        ),
        dmc.NavLink(
            label="Active filled",
            leftSection=get_icon(icon="tabler:activity"),
            rightSection=get_icon(icon="tabler-chevron-right"),
            variant="filled",
            active=True,
        ),
    ],
    style={"width": 240},
)

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


component = html.Div(
    style={"width": 240},
    children=[
        dmc.NavLink(
            label="First parent link",
            leftSection=get_icon(icon="tabler:gauge"),
            childrenOffset=28,
            children=[
                dmc.NavLink(label="First child link"),
                dmc.NavLink(label="Second child link"),
                dmc.NavLink(
                    label="Nested parent link",
                    childrenOffset=28,
                    children=[
                        dmc.NavLink(label="First child link"),
                        dmc.NavLink(label="Second child link"),
                        dmc.NavLink(label="Third child link"),
                    ],
                ),
            ],
        ),
        dmc.NavLink(
            label="Second parent link",
            leftSection=get_icon(icon="tabler:fingerprint"),
            childrenOffset=28,
            opened=True,
            children=[
                dmc.NavLink(label="First child link"),
                dmc.NavLink(label="Second child link"),
                dmc.NavLink(label="Third child link"),
            ],
        ),
    ],
)

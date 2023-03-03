import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "SegmentedControl",
        "data": ["filled", "light", "subtle"],
        "value": "filled",
    },
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
]


def get_icon(icon):
    return DashIconify(icon=icon, height=20)


demo = html.Div(
    [
        dmc.NavLink(
            label="With icon",
            icon=get_icon(icon="bi:house-door-fill"),
        ),
        dmc.NavLink(
            label="With right section",
            icon=get_icon(icon="tabler:gauge"),
            active=True,
            id="navlink-interactive",
            rightSection=get_icon(icon="tabler-chevron-right"),
        ),
    ],
    style={"width": 240},
)

component = create_configurator(demo, controls, cid="navlink-interactive")

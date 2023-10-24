import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from components.configurator import Configurator

TARGET_ID = "interactive-navlink"


def get_icon(icon):
    return DashIconify(icon=icon, height=20)


target = html.Div(
    [
        dmc.NavLink(
            label="With icon",
            icon=get_icon(icon="bi:house-door-fill"),
        ),
        dmc.NavLink(
            label="With right section",
            icon=get_icon(icon="tabler:gauge"),
            active=True,
            id=TARGET_ID,
            rightSection=get_icon(icon="tabler-chevron-right"),
        ),
    ],
    style={"width": 240},
)

configurator = Configurator(target, TARGET_ID)
configurator.add_segmented_control("variant", ["filled", "light", "subtle"], "filled")
configurator.add_colorpicker("color", "indigo")

component = configurator.panel

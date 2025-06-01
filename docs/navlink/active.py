import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from lib.configurator import Configurator

def get_icon(icon):
    return DashIconify(icon=icon, height=20)

# to fix included inside div
target =  dmc.NavLink(
    label="With right section",
    leftSection=get_icon(icon="tabler:gauge"),
    active=True,
    rightSection=get_icon(icon="tabler-chevron-right"),
)

configurator = Configurator(target)

configurator.add_segmented_control("variant", ["filled", "light", "subtle"], "filled")
configurator.add_colorpicker("color", "indigo")

component = configurator.panel

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from utils.configurator import Configurator

target = dmc.Blockquote(
    "Life is like a box of chocolates - you never know what you are going to get"
    "But whatever you get, you should make the most of it and enjoy every moment.",
    cite="- Forest Gump",
    icon=DashIconify(icon="mdi:gift-outline", width=26),
    textWrap="wrap"

)

configurator = Configurator(target)

configurator.add_select("textWrap", ["wrap", "balance", "pretty", "stable", "nowrap"], "wrap")
component = configurator.panel

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Blockquote(
    "Doth mother know you weareth her drapes?",
    cite="- Ironman",
    icon=[DashIconify(icon="codicon:flame", width=30)],
    color="red",
)

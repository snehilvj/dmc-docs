import dash_mantine_components as dmc

from lib.configurator import Configurator
from lib.constants import ALIGN_ITEMS_CSS_PROPERTY, JUSTIFY_CONTENT_CSS_PROPERTY

target = dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    style={"height": 200},
    align="flex-start",
    justify="center",
)

configurator = Configurator(target)

configurator.add_select(
    "align", ALIGN_ITEMS_CSS_PROPERTY, "flex-start"
)
configurator.add_select(
    "justify",
    JUSTIFY_CONTENT_CSS_PROPERTY,
    "center",
)
configurator.add_slider("gap", "sm")


component = configurator.panel

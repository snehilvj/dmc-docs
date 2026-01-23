import dash_mantine_components as dmc

from lib.configurator import Configurator
from lib.constants import FLEX_DIRECTION_CSS_PROPERTY, FLEX_WRAP_CSS_PROPERTY, JUSTIFY_CONTENT_CSS_PROPERTY

target = dmc.Flex(
    [
        dmc.Button("Button 1"),
        dmc.Button("Button 2"),
        dmc.Button("Button 3"),
    ],
    mih=80,
    bg="rgba(0, 0, 0, .3)",
    gap="md",
    justify="flex-start",
    align="flex-start",
    direction="row",
    wrap="wrap",
)

configurator = Configurator(target)
configurator.add_slider("gap", "md")
configurator.add_select("justify", JUSTIFY_CONTENT_CSS_PROPERTY, "center")
configurator.add_select("align", ["flex-start", "center", "flex-end"], "flex-start")
configurator.add_select(
    "direction", FLEX_DIRECTION_CSS_PROPERTY, "row"
)
configurator.add_select("wrap", FLEX_WRAP_CSS_PROPERTY, "wrap")

component = configurator.panel

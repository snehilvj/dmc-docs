import dash_mantine_components as dmc

from lib.configurator import Configurator
from lib.constants import JUSTIFY_CONTENT_CSS_PROPERTY

target = dmc.Group(
    [dmc.Button(val, variant="outline") for val in ["1", "2", "3"]],
    justify="flex-start",
)

configurator = Configurator(target)
configurator.add_select(
    "justify", JUSTIFY_CONTENT_CSS_PROPERTY, "center"
)
configurator.add_slider("gap", "md")
configurator.add_switch("grow", False)

component = configurator.panel

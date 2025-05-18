import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Fieldset(
    children=[
        dmc.TextInput(label="Your name", placeholder="Your name"),
        dmc.TextInput(label="Email", placeholder="Email"),
    ],
    legend="Personal information",
)

configurator = Configurator(target)

configurator.add_select(
    "variant",
    ["default", "filled", "unstyled"],
    "filled",
)
configurator.add_slider("radius", "sm")
configurator.add_switch("disabled", False)

component = configurator.panel

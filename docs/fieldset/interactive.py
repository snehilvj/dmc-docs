import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "fieldset-interactive"

target = dmc.Fieldset(
    children=[
        dmc.TextInput(label="Your name", placeholder="Your name"),
        dmc.TextInput(label="Email", placeholder="Email"),
    ],
    legend="Personal information",
    id=TARGET_ID
)

configurator = Configurator(target, TARGET_ID)

configurator.add_select(
    "variant",
    ["default", "filled", "unstyled"],
    "filled",
)
configurator.add_slider("radius", "sm")
configurator.add_switch("disabled", False)

component = configurator.panel

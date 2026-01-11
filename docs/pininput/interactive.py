import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.PinInput(value="1234")

configurator = Configurator(target, center_component=True)


configurator.add_slider("size", "sm")
configurator.add_number_slider("length", 4, min=1, max=8)
configurator.add_slider("gap", "lg")
configurator.add_switch("mask", False)
configurator.add_text_input("placeholder", "○")
configurator.add_switch("disabled", False)
configurator.add_switch("error", False)


configurator.add_select(
    "type",
    ["alphanumeric", "number" ],
    "alphanumeric",
)

component = configurator.panel

import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.InputWrapper(
        label="Your label",
        description="Your description",
        error="Your error message",
        w=300,
        required=True,
    )

configurator = Configurator(target, center_component=True)

configurator.add_text_input("label", "Your label", placeholder="Label")
configurator.add_text_input("description", "Your description", placeholder="Description")
configurator.add_text_input("error", "Your error message", placeholder="Error")
configurator.add_switch("withAsterisk", True)
component = configurator.panel

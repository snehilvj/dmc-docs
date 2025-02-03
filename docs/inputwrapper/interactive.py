import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-input-wrapper"

target = dmc.Center(
    dmc.InputWrapper(
        label="Your label",
        description="Your description",
        error="Your error message",
        w=300,
        required=True,
        id=TARGET_ID,
    )
)

configurator = Configurator(target, TARGET_ID)

configurator.add_text_input("label", "Your label", placeholder="Label")
configurator.add_text_input("description", "Your description", placeholder="Description")
configurator.add_text_input("error", "Your error message", placeholder="Error")
configurator.add_switch("withAsterisk", True)
component = configurator.panel

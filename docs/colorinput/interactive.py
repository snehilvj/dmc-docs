import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-color-input"
target = dmc.Center(
    dmc.ColorInput(
        label="Your favorite color",
        placeholder="Pick color",
        w=250,
        id=TARGET_ID,
    )
)

configurator = Configurator(target, TARGET_ID, "ColorInput")
configurator.add_text_input(
    "placeholder", "Pick color", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Your favorite color", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "default")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("withAsterisk", True)
configurator.add_switch("disabled", False)
configurator.add_switch("withEyeDropper", False)

component = configurator.panel

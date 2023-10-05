import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.PasswordInput(
    label="Enter your password",
    placeholder="Password",
    description="Password must include at least one letter, number and special character",
    required=True,
)

configurator = Configurator(target)
configurator.add_text_input("placeholder", "Password", **{"placeholder": "Placeholder"})
configurator.add_text_input("label", "Enter your password", **{"placeholder": "Label"})
configurator.add_text_input(
    "description",
    "Password must include at least one letter, number and special character",
    **{"placeholder": "Description"}
)
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "filled")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("required", True)

component = configurator.panel

import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.TextInput(
    label="Full Name", placeholder="Your Name", style={"width": 300}, required=True
)

configurator = Configurator(target)
configurator.add_text_input(
    "placeholder", "Your Name", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Full Name", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("required", True)

component = configurator.panel

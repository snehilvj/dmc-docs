import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Select(
    label="Select framework",
    data=["React", "Angular", "Svelte", "Vue"],
    value="Vue",
    clearable=True,
    style={"width": 200},
)

configurator = Configurator(target)
configurator.add_text_input("placeholder", "Pick one", **{"placeholder": "Placeholder"})
configurator.add_text_input("label", "Select framework", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "filled")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("disabled", False)
configurator.add_switch("withAsterisk", True)

component = configurator.panel

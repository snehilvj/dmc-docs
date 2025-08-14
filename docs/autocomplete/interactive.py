import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Autocomplete(
        label="",
        placeholder="placeholder",
        data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
        id="autocomplete"
    )

configurator = Configurator(target, center_component=True)

configurator.add_text_input(
    "placeholder", "Autocomplete placeholder", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Input Label", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "default")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("withAsterisk", True)
configurator.add_switch("disabled", False)
configurator.add_switch("clearable", True)


component = configurator.panel

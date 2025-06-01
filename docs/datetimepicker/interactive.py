import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.DateTimePicker(
        label="Pick a date and time",
        placeholder="Pick date and time",
        w=250,
    )

configurator = Configurator(target, center_component=True)

configurator.add_text_input(
    "placeholder", "Pick date and time", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Pick date and time", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "default")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("withAsterisk", True)
configurator.add_switch("disabled", False)


component = configurator.panel

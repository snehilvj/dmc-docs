import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.TimeInput(
    label="Start time", description="Enter start time for processing"
)

configurator = Configurator(target)

configurator.add_text_input("label", "Current Time", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "default")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("disabled", False)
configurator.add_switch("withAsterisk", True)
component = configurator.panel

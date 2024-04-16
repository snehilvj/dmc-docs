import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-date-input"
target = dmc.Center(
    dmc.DateInput(
        label="Enter date", placeholder="Enter date", style={"width": 350}, id=TARGET_ID
    )
)

configurator = Configurator(target, TARGET_ID)
configurator.add_text_input(
    "placeholder", "Enter date", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Enter date", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_select("variant", ["default", "filled", "unstyled"], "default")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("withAsterisk", True)
configurator.add_switch("disabled", False)
configurator.add_switch("clearable", True)


component = configurator.panel

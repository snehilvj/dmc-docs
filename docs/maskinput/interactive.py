import dash_mantine_components as dmc

from utils.configurator import Configurator

target = dmc.MaskInput(
        label="Input label", placeholder="(___) ___-____", w=300, required=True, mask="(999) 999-9999"
    )

configurator = Configurator(target, center_component=True)

configurator.add_text_input(
    "placeholder", "(___) ___-____", **{"placeholder": "Placeholder"}
)
configurator.add_text_input("label", "Input label", **{"placeholder": "Label"})
configurator.add_text_input("description", "Input description", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_text_input("success", "", **{"placeholder": "Success"})
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_segmented_control("variant", ["default", "filled", "unstyled"], "default")
configurator.add_switch("required", True)

component = configurator.panel

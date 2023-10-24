import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-stepper-color"

target = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")

component = configurator.panel

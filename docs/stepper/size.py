import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-stepper-size"

target = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID)

configurator.add_number_input("iconSize", 42)

component = configurator.panel

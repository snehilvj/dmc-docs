import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
)

configurator = Configurator(target)

configurator.add_number_input("iconSize", 42)

component = configurator.panel

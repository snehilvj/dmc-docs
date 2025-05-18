import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ]
)

configurator = Configurator(target, center_component=True)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")

component = configurator.panel

import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [{"property": "iconSize", "component": "NumberInput", "value": 42}]

demo = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
)

component = create_configurator(demo, controls, center=False)

import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {"property": "radius", "component": "DemoSlider", "value": "xl"},
]

demo = dmc.Stepper(
    active=1,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
)

component = create_configurator(demo, controls, center=False)

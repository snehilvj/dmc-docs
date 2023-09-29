import dash_mantine_components as dmc

component = dmc.Stepper(
    active=1,
    orientation="vertical",
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
        dmc.StepperStep(label="Final step", description="Get full access"),
    ],
)

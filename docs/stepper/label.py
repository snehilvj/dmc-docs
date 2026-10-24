import dash_mantine_components as dmc

component = dmc.Stepper(
    [
        dmc.StepperStep(label="Account"),
        dmc.StepperStep(label="Verification"),
        dmc.StepperStep(label="Access"),
    ],
    id="stepper",
    active=1,
    labelPosition="bottom",
)

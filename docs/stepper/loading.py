import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Stepper(
            active=1,
            children=[
                dmc.StepperStep(
                    label="First step",
                    description="Create an account",
                    children=dmc.Text("Step 1 content: Create an account", ta="center"),
                ),
                dmc.StepperStep(
                    label="Second step",
                    description="Verify email",
                    children=dmc.Text("Step 2 content: Verify email", ta="center"),
                    loading=True,
                ),
                dmc.StepperStep(
                    label="Final step",
                    description="Get full access",
                    children=dmc.Text("Step 3 content: Get full access", ta="center"),
                ),
            ],
        ),
    ]
)

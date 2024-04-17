import dash_mantine_components as dmc
from dash import html, Output, Input, State, ctx, callback

min_step = 0
max_step = 3
active = 1

component = html.Div(
    [
        dmc.Stepper(
            id="stepper-basic-usage",
            active=active,
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
                ),
                dmc.StepperStep(
                    label="Final step",
                    description="Get full access",
                    children=dmc.Text("Step 3 content: Get full access", ta="center"),
                ),
                dmc.StepperCompleted(
                    children=dmc.Text(
                        "Completed, click back button to get to previous step",
                        ta="center",
                    )
                ),
            ],
        ),
        dmc.Group(
            justify="center",
            mt="xl",
            children=[
                dmc.Button("Back", id="back-basic-usage", variant="default"),
                dmc.Button("Next step", id="next-basic-usage"),
            ],
        ),
    ]
)


@callback(
    Output("stepper-basic-usage", "active"),
    Input("back-basic-usage", "n_clicks"),
    Input("next-basic-usage", "n_clicks"),
    State("stepper-basic-usage", "active"),
    prevent_initial_call=True,
)
def update(back, next_, current):
    button_id = ctx.triggered_id
    step = current if current is not None else active
    if button_id == "back-basic-usage":
        step = step - 1 if step > min_step else step
    else:
        step = step + 1 if step < max_step else step
    return step

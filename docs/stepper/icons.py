import dash_mantine_components as dmc
from dash import callback, Output, Input, State, ctx
from dash_iconify import DashIconify

min_step = 0
max_step = 3
active = 1


def get_icon(icon):
    return DashIconify(icon=icon, height=20)


component = dmc.Container(
    [
        dmc.Stepper(
            id="stepper-custom-icons",
            active=active,
            children=[
                dmc.StepperStep(
                    label="First step",
                    description="Create an account",
                    icon=get_icon(icon="material-symbols:account-circle"),
                    progressIcon=get_icon(icon="material-symbols:account-circle"),
                    completedIcon=get_icon(icon="mdi:account-check"),
                    children=[
                        dmc.Text("Step 1 content: Create an account", ta="center")
                    ],
                ),
                dmc.StepperStep(
                    label="Second step",
                    description="Verify email",
                    icon=get_icon(icon="ic:outline-email"),
                    progressIcon=get_icon(icon="ic:outline-email"),
                    completedIcon=get_icon(
                        icon="material-symbols:mark-email-read-rounded"
                    ),
                    children=[dmc.Text("Step 2 content: Verify email", ta="center")],
                ),
                dmc.StepperStep(
                    label="Final step",
                    description="Get full access",
                    icon=get_icon(icon="material-symbols:lock-outline"),
                    progressIcon=get_icon(icon="material-symbols:lock-outline"),
                    completedIcon=get_icon(icon="material-symbols:lock-open-outline"),
                    children=[dmc.Text("Step 3 content: Get full access", ta="center")],
                ),
                dmc.StepperCompleted(
                    children=[
                        dmc.Text(
                            "Completed, click back button to get to previous step",
                            ta="center",
                        )
                    ]
                ),
            ],
        ),
        dmc.Group(
            justify="center",
            mt="xl",
            children=[
                dmc.Button("Back", id="back-custom-icons", variant="default"),
                dmc.Button("Next step", id="next-custom-icons"),
            ],
        ),
    ]
)


@callback(
    Output("stepper-custom-icons", "active"),
    Input("back-custom-icons", "n_clicks"),
    Input("next-custom-icons", "n_clicks"),
    State("stepper-custom-icons", "active"),
    prevent_initial_call=True,
)
def update_with_icons(back, next_, current):
    button_id = ctx.triggered_id
    step = current if current is not None else active
    if button_id == "back-custom-icons":
        step = step - 1 if step > min_step else step
    else:
        step = step + 1 if step < max_step else step
    return step

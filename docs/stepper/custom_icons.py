import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import callback, Output, Input, State, ctx, no_update

minStep = 0
maxStep = 3
act = 0

iconHeight = 28
iconWidth = 28
iconColor = "#228BE6"

component = dmc.Container([
    dmc.Stepper(
        id="stepper_custom_icons",
        active=act,
        breakpoint="sm",
        children=[
            dmc.StepperStep(
                label="First step",
                description="Create an account",
                icon=DashIconify(icon="material-symbols:account-circle", width=iconWidth, height=iconHeight, color=iconColor),
                progressIcon=DashIconify(icon="material-symbols:account-circle", width=iconWidth, height=iconHeight, color=iconColor),
                completedIcon=DashIconify(icon="mdi:account-check", width=iconWidth, height=iconHeight),
                children=[dmc.Text('Step 1 content: Create an account',align="center", weight=700)]
            ),
            dmc.StepperStep(
                label="Second step",
                description="Verify email",
                icon=DashIconify(icon="ic:outline-email", width=iconWidth, height=iconHeight, color=iconColor),
                progressIcon=DashIconify(icon="ic:outline-email", width=iconWidth, height=iconHeight, color=iconColor),
                completedIcon=DashIconify(icon="material-symbols:mark-email-read-rounded", width=iconWidth, height=iconHeight),
                children=[dmc.Text('Step 2 content: Verify email',align="center", weight=700)]
            ),
            dmc.StepperStep(
                label="Final step",
                description="Get full access",
                icon=DashIconify(icon="material-symbols:lock-outline", width=iconWidth, height=iconHeight, color=iconColor),
                progressIcon=DashIconify(icon="material-symbols:lock-outline", width=iconWidth, height=iconHeight, color=iconColor),
                completedIcon=DashIconify(icon="material-symbols:lock-open-outline", width=iconWidth, height=iconHeight),
                children=[dmc.Text('Step 3 content: Get full access',align="center", weight=700)]
            ),
            dmc.StepperCompleted(children=[dmc.Text('Completed, click back button to get to previous step', align="center", weight=700)]),

        ],
    ),
    dmc.Group(position="center",mt="xl", children=[
        dmc.Button("Back", id="back_custom_icons", variant="default"),
        dmc.Button("Next step", id="next_custom_icons"),
    ])
])

@callback(
    Output("stepper_custom_icons","active"),
    Input("back_custom_icons", "n_clicks"),
    Input("next_custom_icons", "n_clicks"),
    State("stepper_custom_icons","active"),
    prevent_initial_call=True)
def btn_actions(back, next, current):
    
    button_id = ctx.triggered_id 

    step = current if current != None else act

    match(button_id):
        case 'back_custom_icons':
            step = step - 1 if step > minStep else step
            return step
        case 'next_custom_icons':
            step = step + 1 if step < maxStep else step
            return step

            
            

    
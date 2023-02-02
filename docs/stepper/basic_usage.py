
from dash import html, Output, Input, State, ctx, no_update, callback
import dash_mantine_components as dmc

minStep = 0
maxStep = 3
act = 0

component = html.Div([dmc.Stepper(
        id="stepper_basic_usage",
        active=act,
        breakpoint="sm",
        children=[
            dmc.StepperStep(
                label="First step",
                description="Create an account",
                children=[dmc.Text('Step 1 content: Create an account',align="center", weight=700)]
            ),
            dmc.StepperStep(
                label="Second step",
                description="Verify email",
                children=[dmc.Text('Step 2 content: Verify email',align="center", weight=700)]
            ),
            dmc.StepperStep(
                label="Final step",
                description="Get full access",
                children=[dmc.Text('Step 3 content: Get full access',align="center", weight=700)]
            ),
            dmc.StepperCompleted(children=[dmc.Text('Completed, click back button to get to previous step', align="center", weight=700)]),
        ],
    ),
    dmc.Group(position="center",mt="xl", children=[
        dmc.Button("Back", id="back_basic_usage", variant="default"),
        dmc.Button("Next step", id="next_basic_usage"),
    ])])

@callback(
    Output("stepper_basic_usage","active"),
    Input("back_basic_usage", "n_clicks"),
    Input("next_basic_usage", "n_clicks"),
    State("stepper_basic_usage","active"),
    prevent_initial_call=True)
def btn_actions(back, next, current):
    
    button_id = ctx.triggered_id 

    step = current if current != None else act

    match(button_id):
        case 'back_basic_usage':
            step = step - 1 if step > minStep else step
            return step
        case 'next_basic_usage':
            step = step + 1 if step < maxStep else step
            return step

        

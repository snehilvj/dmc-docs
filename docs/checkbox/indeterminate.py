

from dash import  html,  Input, Output,  callback, ALL, ctx
import dash_mantine_components as dmc

initial_values = [
    {"label": "Receive email notifications", "checked": False},
    {"label": "Receive sms notifications", "checked": False},
    {"label": "Receive push notifications", "checked": False},
]

component = html.Div([
    dmc.Checkbox(
        id="all-notifications",
        label="Receive all notifications",
        checked=False,
        indeterminate=False
    ),
    html.Div([
        dmc.Checkbox(
            id={"type": "notification-item", "index": i},
            label=item["label"],
            checked=item["checked"],
            style={"marginTop": "5px", "marginLeft": "33px"}
        )
        for i, item in enumerate(initial_values)
    ])
])



@callback(
    Output("all-notifications", "checked"),
    Output("all-notifications", "indeterminate"),
    Output({"type": "notification-item", "index": ALL}, "checked"),
    Input("all-notifications", "checked"),
    Input({"type": "notification-item", "index": ALL}, "checked"),
    prevent_initial_callback=True
)
def update_main_checkbox(all_checked, checked_states):
    # handle "all" checkbox"
    if ctx.triggered_id == 'all-notifications':
        checked_states = [all_checked] * len(checked_states)

    # handled individual check boxes
    all_checked_states = all(checked_states)
    indeterminate = any(checked_states) and not all_checked_states
    return all_checked_states, indeterminate, checked_states


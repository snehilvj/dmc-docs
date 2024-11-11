

from dash import  html,  Input, Output,  callback, ALL
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
    Input({"type": "notification-item", "index": ALL}, "checked")
)
def update_main_checkbox(checked_states):
    all_checked = all(checked_states)
    indeterminate = any(checked_states) and not all_checked
    return all_checked, indeterminate

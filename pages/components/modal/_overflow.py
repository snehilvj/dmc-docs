import dash_mantine_components as dmc
from dash import callback  # no-prism
from dash import html, Output, Input, State

paragraph = (
    """Dash apps give a point-&-click interface to models written in Python, vastly expanding the notion of what's 
    possible in a traditional 'dashboard.' With Dash apps, data scientists and engineers put complex Python analytics 
    in the hands of business decision-makers and operators. """
    * 10
)

component = html.Div(
    [
        dmc.Modal(
            id="modal-outside",
            title="Outside Overflow",
            overflow="outside",
            children=[dmc.Text(paragraph)],
        ),
        dmc.Modal(
            id="modal-inside",
            title="Inside Overflow",
            overflow="inside",
            children=[dmc.Text(paragraph)],
        ),
        dmc.Group(
            [
                dmc.Button("Outside Overflow", id="modal-outside-button"),
                dmc.Button("Inside Overflow", id="modal-inside-button"),
            ]
        ),
    ]
)


def toggle_modal(n_clicks, opened):
    return not opened


for overflow in ["outside", "inside"]:
    callback(
        Output(f"modal-{overflow}", "opened"),
        Input(f"modal-{overflow}-button", "n_clicks"),
        State(f"modal-{overflow}", "opened"),
        prevent_initial_call=True,
    )(toggle_modal)

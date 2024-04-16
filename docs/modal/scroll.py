import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

paragraph = (
    """Dash apps give a point-&-click interface to models written in Python, vastly expanding the notion of what's 
        possible in a traditional 'dashboard.' With Dash apps, data scientists and engineers put complex Python analytics 
        in the hands of business decision-makers and operators. """
    * 10
)

component = html.Div(
    [
        dmc.Modal(
            id="modal-scroll",
            title="Modal with Scroll",
            zIndex=10000,
            children=[dmc.Text(paragraph)],
        ),
        dmc.Button("Modal with Scroll", id="modal-scroll-button"),
    ]
)


@callback(
    Output("modal-scroll", "opened"),
    Input("modal-scroll-button", "n_clicks"),
    State("modal-scroll", "opened"),
    prevent_initial_call=True,
)
def toggle_modal(n_clicks, opened):
    return not opened

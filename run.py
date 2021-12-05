import dash
from dash import Dash, html, Output, Input, State
from datetime import datetime
import dash_mantine_components as dmc
from utils import create_component_title
from components.accordion import accordion
from components.affix import affix
from components.alert import alert
from components.badge import badge
from components.button import button
from components.checkbox import checkbox
from components.chips import chips
from components.datepicker import datepicker
from components.divider import divider
from components.drawer import drawer

app = Dash(__name__)


app.layout = dmc.Container(
    style={"padding": 20},
    children=[
        dmc.Group(
            position="apart",
            children=[
                dmc.Text(
                    "Dash Mantine Components",
                    variant="gradient",
                    style={"fontSize": 35},
                    gradient={"from": "indigo", "to": "cyan", "deg": 45},
                ),
                dmc.Anchor(
                    dmc.Button("GitHub", variant="outline"),
                    size="xl",
                    href="https://github.com/snehilvj/dash-mantine-components",
                ),
            ],
        ),
        # components
        accordion,
        affix,
        alert,
        badge,
        button,
        checkbox,
        chips,
        datepicker,
        divider,
        drawer,
    ],
)


# callbacks
@app.callback(
    Output("alert", "show"),
    Input("alert-button", "n_clicks"),
    State("alert", "show"),
    prevent_initial_call=True,
)
def restart(n_clicks, show):
    return not show


@app.callback(
    Output("drawer", "opened"),
    Input("drawer-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer(n_clicks):
    return True


if __name__ == "__main__":
    app.run_server(debug=True)

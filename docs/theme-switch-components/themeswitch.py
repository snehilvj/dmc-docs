
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output, clientside_callback, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

theme_toggle = dmc.ActionIcon(
    [
        dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
        dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
    ],
    variant="transparent",
    color="yellow",
    id="color-scheme-toggle",
    size="lg",
)


component=dmc.Group([
    dmc.Text("Theme Switch Demo"),
    theme_toggle
])


clientside_callback(
    """
    (n) => {
        document.documentElement.setAttribute(
            'data-mantine-color-scheme',
            (n % 2) ? 'dark' : 'light'
        );
        return window.dash_clientside.no_update      
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "n_clicks"),
)

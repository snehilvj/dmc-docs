import dash_mantine_components as dmc
from dash import Input, Output, clientside_callback
from dash_iconify import DashIconify

theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color= "var(--mantine-color-yellow-8)"),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color= "var(--mantine-color-yellow-6)"),
    id="color-scheme-switch",
    persistence=True,
    color="grey",
)

component=dmc.Group([
    dmc.Text("Theme Switch Demo"),
    theme_toggle
])

clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-switch", "id"),
    Input("color-scheme-switch", "checked"),
)

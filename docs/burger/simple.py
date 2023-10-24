import dash_mantine_components as dmc
from dash import Input, Output, callback, html

component = html.Div(
    [dmc.Burger(id="burger-button", opened=False), dmc.Text(id="burger-state", mt="md")]
)


@callback(Output("burger-state", "children"), Input("burger-button", "opened"))
def open_burger(opened):
    return str(opened)

from dash import Input, Output, callback, html
import dash_mantine_components as dmc

component = html.Div(
    [dmc.Burger(id="burger-button", opened=False), dmc.Text(id="burger-state", mt="md")]
)


@callback(Output("burger-state", "children"), Input("burger-button", "opened"))
def open(opened):
    return str(opened)

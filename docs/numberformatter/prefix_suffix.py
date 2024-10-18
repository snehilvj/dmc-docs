from dash import html
import dash_mantine_components as dmc

component = html.Div([
    html.Div(["With prefix: ", dmc.NumberFormatter(value=100, prefix="$")]),
    html.Div(["With suffix: ", dmc.NumberFormatter(value=100, suffix=" RUB")]),
])

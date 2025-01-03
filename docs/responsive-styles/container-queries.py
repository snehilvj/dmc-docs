from dash import html
import dash_mantine_components as dmc

component = html.Div(
    className="container-query-demo-root",
    children=html.Div(
        "Resize parent element to see container query in action",
        className="container-query-demo-child"
    )
)

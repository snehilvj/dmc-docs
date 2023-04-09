import dash_mantine_components as dmc
from dash import callback, Output, Input, html

component = html.Div(
    [
        dmc.Select(
            id="creatable-select",
            creatable=True,
            searchable=True,
            style={"width": 200},
            data=["react", "flask"],
        ),
        dmc.Text(id="new-items", mt=20),
    ]
)


@callback(Output("new-items", "children"), Input("creatable-select", "data"))
def new_item(data):
    return str(data)

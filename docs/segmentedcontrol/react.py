import dash_mantine_components as dmc
from dash import Output, Input, html, callback
from dash_iconify import DashIconify

data = [
    ["Preview", "tabler:eye"],
    ["Code", "tabler:code"],
    ["Export", "tabler:external-link"],
]

component = html.Div(
    [
        dmc.SegmentedControl(
            id="segmented-with-react-nodes",
            value="Preview",
            data=[
                {
                    "value": v,
                    "label": dmc.Center(
                        [DashIconify(icon=icon, width=16), html.Span(v)],
                        style={"gap": 10},
                    ),
                }
                for v, icon in data
            ],
            mb=10,
        ),
        dmc.Text(id="segmented--value-data"),
    ]
)


@callback(
    Output("segmented--value-data", "children"),
    Input("segmented-with-react-nodes", "value"),
)
def update_value(value):
    return value

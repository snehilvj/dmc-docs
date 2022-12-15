import dash_mantine_components as dmc

component = dmc.Footer(
    height=60,
    fixed=True,
    children=[dmc.Text("Company Logo")],
    style={"backgroundColor": "#9c86e2"},
)


from dash import Input, Output, callback
import dash_mantine_components as dmc

component = dmc.Box([
        dmc.CheckboxCard(
            id="checkbox-card",
            withBorder=True,
            p="md",
            checked=True,
            children=[
                dmc.Center([
                    dmc.CheckboxIndicator(),
                    dmc.Text("CheckboxCard", size="xl", pl="sm"),
                ], inline=True),
            ]
        ),
        dmc.Box(id="checkbox-card-out"),
    ], p="lg")


@callback(
    Output("checkbox-card-out", "children"),
    Input("checkbox-card", "checked")
)
def update(checked):
   return f"Checked? {checked}"

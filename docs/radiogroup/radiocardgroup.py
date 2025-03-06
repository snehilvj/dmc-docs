
from dash import  Input, Output, callback
import dash_mantine_components as dmc

def make_radiocard(label, description):
    return dmc.RadioCard(
        withBorder=True,
        p="md",
        mt="md",
        className="checkboxcard-root",
        value=label,
        children=[
            dmc.Group([
                dmc.RadioIndicator(),
                dmc.Box([
                    dmc.Text(label, lh="1.3", fz="md", fw="bold" ),
                    dmc.Text(description, size="sm", c="dimmed"),
                ])
            ], wrap="nowrap", align="flex-start"),
        ]
    )


component = dmc.Box([
    dmc.RadioGroup(
        id="radiocard-group",
        label= "RadioGroup label",
        value="RadioCard 1",
        description="This is a RadioGroup description",
        deselectable=True,
        children=[
            make_radiocard(f"RadioCard {i}", f"RadioCard description {i}")
            for i in range(1, 5)
        ]
    ),
    dmc.Box(id="radio-group-out"),
])


@callback(
    Output("radiocard-group-out", "children"),
    Input("radiocard-group", "value")
)
def update(checked):
   return f"Selected: {checked}"

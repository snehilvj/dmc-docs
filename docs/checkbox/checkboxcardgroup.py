
from dash import Input, Output, callback
import dash_mantine_components as dmc

def make_checkboxcard(label, description):
    return dmc.CheckboxCard(
        withBorder=True,
        p="md",
        mt="md",
        className="checkboxcard-root",
        value=label,
        children=[
            dmc.Group([
                dmc.CheckboxIndicator(),
                dmc.Box([
                    dmc.Text(label, lh="1.3", fz="md", fw="bold" ),
                    dmc.Text(description, size="sm", c="dimmed"),
                ])
            ], wrap="nowrap", align="flex-start"),
        ]
    )


component = dmc.Box([
    dmc.CheckboxGroup(
        id="checkbox-card-group",
        label= "CheckboxGroup label",
        value=["CheckboxCard 1"],
        description="This is a CheckboxGroup description",
        children=[
            make_checkboxcard(f"CheckboxCard {i}", f"Checkbox description {i}")
            for i in range(1, 5)
        ]
    ),
    dmc.Box(id="checkbox-card-group-out"),
], p="lg")


@callback(
    Output("checkbox-card-group-out", "children"),
    Input("checkbox-card-group", "value")
)
def update(checked):
   return f"Checked? {checked}"


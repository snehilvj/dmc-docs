import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.CheckboxGroup(
            id="checkbox-group",
            label="Select your favorite framework/library",
            description="This is anonymous",
            orientation="horizontal",
            withAsterisk=True,
            offset="md",
            mb=10,
            children=[
                dmc.Checkbox(label="React", value="react"),
                dmc.Checkbox(label="Vue", value="vue"),
                dmc.Checkbox(label="Svelte", value="svelte"),
                dmc.Checkbox(label="Angular", value="angular"),
            ],
            value=["react", "vue"],
        ),
        dmc.Text(id="checkbox-group-output"),
    ]
)


@callback(Output("checkbox-group-output", "children"), Input("checkbox-group", "value"))
def checkbox(value):
    return ", ".join(value) if value else None

import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.TagsInput(
            label="Select frameworks",
            placeholder="Select all you like!",
            id="framework-tags-input",
            value=["ng", "vue"],
            w=400,
            mb=10,
        ),
        dmc.Text(id="tags-input-value"),
    ]
)


@callback(
    Output("tags-input-value", "children"), Input("framework-tags-input", "value")
)
def select_value(value):
    return ", ".join(value)

import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.TagsInput(
            label="Value is accepted on blur",
            placeholder="Select all you like!",
            id="framework-tags-input1",
            value=["Pandas", "NumPy"],
            w=400,
            mb=10,
        ),
        dmc.Text(id="tags-input-value1", mb="xl"),
        dmc.TagsInput(
            label="Value IS NOT accepted on blur",
            placeholder="Select all you like!",
            id="framework-tags-input2",
            value=["Pandas", "NumPy"],
            acceptValueOnBlur=False,
            w=400,
            mb=10,
        ),
        dmc.Text(id="tags-input-value2"),
    ]
)


@callback(
    Output("tags-input-value1", "children"), Input("framework-tags-input1", "value")
)
def select_value(value):
    return f"You selected {value}"


@callback(
    Output("tags-input-value2", "children"), Input("framework-tags-input2", "value")
)
def select_value(value):
    return f"You selected {value}"


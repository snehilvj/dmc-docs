import dash_mantine_components as dmc
from dash import html, Output, Input, callback

data = [["react", "React"], ["ng", "Angular"], ["svelte", "Svelte"], ["vue", "Vue"]]

component = html.Div(
    [
        dmc.RadioGroup(
            [dmc.Radio(l, value=k) for k, l in data],
            id="radiogroup-simple",
            value="react",
            label="Select your favorite framework/library",
            size="sm",
            mt=10,
        ),
        dmc.Text(id="radio-output"),
    ]
)


@callback(Output("radio-output", "children"), Input("radiogroup-simple", "value"))
def choose_framework(value):
    return value

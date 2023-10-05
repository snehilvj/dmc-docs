import dash_mantine_components as dmc
from dash import html, Output, Input, callback

data = [["react", "React"], ["ng", "Angular"], ["svelte", "Svelte"], ["vue", "Vue"]]

component = html.Div(
    [
        dmc.RadioGroup(
            children=dmc.Group([dmc.Radio(l, value=k) for k, l in data]),
            id="radiogroup-simple",
            value="react",
            label="Select your favorite framework/library",
            size="sm",
            mt=10,
        ),
        dmc.RadioGroup(
            children=dmc.Stack([dmc.Radio(l, value=k) for k, l in data]),
            id="radiogroup-simple",
            value="react",
            label="Select your favorite framework/library",
            size="sm",
            mt=10,
        ),
    ]
)

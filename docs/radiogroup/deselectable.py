import dash_mantine_components as dmc
from dash import html

data = [["react", "React"], ["ng", "Angular"], ["svelte", "Svelte"], ["vue", "Vue"]]

component = html.Div(
    [
        dmc.RadioGroup(
            children=dmc.Group([dmc.Radio(l, value=k) for k, l in data], my=10),
            id="radiogroup-simple",
            value="react",
            label="Select your favorite framework/library",
            size="sm",
            my=10,
            deselectable=True
        ),

    ]
)

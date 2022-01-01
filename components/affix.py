import dash_mantine_components as dmc
from dash import html
from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Affix.__doc__)

layout = html.Div(
    children=[
        ComponentName("Affix"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple Example",
            caption="Look at the bottom right!",
            code="""import dash_mantine_components as dmc

component = dmc.Affix(
    dmc.Button("I'm in an Affix Component"), position={"bottom": 20, "right": 20}
)""",
        ),
        ComponentReference(apidocs),
    ]
)

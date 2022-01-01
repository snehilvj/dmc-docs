import dash_mantine_components as dmc
from dash import html

from .title import Title


def ComponentReference(doc):
    return html.Div(
        [
            Title("Keyword arguments"),
            dmc.Prism(
                language="git",
                code=doc,
                noCopy=True,
                style={"whiteSpace": "pre-wrap", "marginBottom": 100},
            ),
        ]
    )

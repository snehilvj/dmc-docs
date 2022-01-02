import dash_mantine_components as dmc
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
    Title,
    SubText,
    OnlyComponentBlock,
    OnlyCodeBlock,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Divider.__doc__)

layout = html.Div(
    children=[
        ComponentName("Divider"),
        ComponentDescription(description),
        Title("Simple Divider"),
        SubText(
            dcc.Markdown(
                "The simplest divider is basically an html.Hr component. dmc.Divider can be customized by providing a "
                "`label`, setting the label's `position` and changing its size or style or color. "
            )
        ),
        OnlyComponentBlock(
            [
                html.Div(
                    [
                        dmc.Divider(variant="solid"),
                        dmc.Space(h=20),
                        dmc.Divider(variant="dashed"),
                        dmc.Space(h=20),
                        dmc.Divider(variant="dotted"),
                    ]
                )
            ]
        ),
        OnlyCodeBlock(
            """import dash_mantine_components as dmc
from dash import html

component = html.Div([
    dmc.Divider(),
    dmc.Divider(variant="dashed"),
    dmc.Divider(variant="dotted"),
])"""
        ),
        dmc.Space(h=40),
        Title("With Label"),
        SubText(
            dcc.Markdown(
                "You can provide `label` and `labelPosition` to customize dmc.Divider."
            )
        ),
        OnlyComponentBlock(
            [
                html.Div(
                    [
                        dmc.Divider(label="Click on update button to refresh"),
                        dmc.Space(h=20),
                        dmc.Divider(
                            label="Divider with centered content",
                            labelPosition="center",
                        ),
                        dmc.Space(h=20),
                        dmc.Divider(
                            label="Divider with content on the right",
                            labelPosition="right",
                        ),
                    ]
                )
            ]
        ),
        OnlyCodeBlock(
            """import dash_mantine_components as dmc
from dash import html

component = html.Div([
    dmc.Divider(label="Click on update button to refresh"),
    dmc.Divider(
        label="Divider with centered content",
        labelPosition="center",
    ),
    dmc.Divider(
        label="Divider with content on the right",
        labelPosition="right",
    ),
])"""
        ),
        dmc.Space(h=40),
        Title("Different Sizes"),
        SubText(
            dcc.Markdown("Set the `size` property to change the size of the divider.")
        ),
        OnlyComponentBlock(
            [
                html.Div(
                    [
                        dmc.Divider(size="xs"),
                        dmc.Space(h=20),
                        dmc.Divider(size="sm"),
                        dmc.Space(h=20),
                        dmc.Divider(size="md"),
                        dmc.Space(h=20),
                        dmc.Divider(size="lg"),
                        dmc.Space(h=20),
                        dmc.Divider(size="xl"),
                        dmc.Space(h=20),
                        dmc.Divider(size=10),
                    ]
                )
            ]
        ),
        OnlyCodeBlock(
            """import dash_mantine_components as dmc
from dash import html

component = html.Div([
    dmc.Divider(size="xs"),
    dmc.Divider(size="sm"),
    dmc.Divider(size="md"),
    dmc.Divider(size="lg"),
    dmc.Divider(size="xl"),
    dmc.Divider(size=10),
])"""
        ),
        dmc.Space(h=40),
        ComponentBlock(
            title="Vertical Divider",
            caption=dcc.Markdown(
                """Divider can be used in vertical orientations as well by setting `orientation="vertical"` and 
                providing it some height."""
            ),
            code="""import dash_mantine_components as dmc

component = dmc.Group([
    dmc.Badge("Badge 1"),
    dmc.Divider(orientation="vertical", style={"height": 20}),
    dmc.Badge("Badge 2"),
    dmc.Divider(orientation="vertical", style={"height": 20}),
    dmc.Badge("Badge 3"),
])""",
        ),
        ComponentBlock(
            title="With Color",
            caption=dcc.Markdown(
                """Set Divider color from one of the colors of Mantine default theme."""
            ),
            code="""import dash_mantine_components as dmc

component = dmc.Divider(color="violet")""",
        ),
        ComponentReference(apidocs),
    ]
)

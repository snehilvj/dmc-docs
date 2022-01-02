import dash_mantine_components as dmc
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
    OnlyComponentBlock,
    OnlyCodeBlock,
    SubText,
    Title,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Checkbox.__doc__)

layout = html.Div(
    children=[
        ComponentName("Checkbox"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple checkbox",
            caption=dcc.Markdown("Use the property `checked` in the callbacks."),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input

component = html.Div([
    dmc.Checkbox(
        id="checkbox",
        label="I agree to sell my privacy",
    ),
    dmc.Space(h=10),
    dmc.Text(id="checkbox-output"),
])


@app.callback(
    Output("checkbox-output", "children"),
    Input("checkbox", "checked")
)
def checkbox(checked):
    return "True" if checked else "False" """,
        ),
        Title("Different sizes"),
        SubText(
            dcc.Markdown(
                "Choose from one of the following sizes: `xs, sm, md, lg, xl`."
            )
        ),
        OnlyComponentBlock(
            [
                html.Div(
                    [
                        dmc.Checkbox(
                            label="I agree to sell my privacy",
                            size="xs",
                            class_name="checkbox",
                            checked=True,
                        ),
                        dmc.Checkbox(
                            label="I agree to sell my privacy",
                            size="sm",
                            class_name="checkbox",
                            checked=True,
                        ),
                        dmc.Checkbox(
                            label="I agree to sell my privacy",
                            size="md",
                            class_name="checkbox",
                            checked=True,
                        ),
                        dmc.Checkbox(
                            label="I agree to sell my privacy",
                            size="lg",
                            class_name="checkbox",
                            checked=True,
                        ),
                        dmc.Checkbox(
                            label="I agree to sell my privacy", size="xl", checked=True
                        ),
                    ]
                )
            ]
        ),
        OnlyCodeBlock(
            """import dash_mantine_components as dmc
from dash import html

html.Div(
    [
        dmc.Checkbox(label="I agree to sell my privacy", size="xs", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="sm", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="md", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="lg", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="xl", checked=True),
    ]
)"""
        ),
        dmc.Space(h=40),
        Title("Different colors"),
        SubText(dcc.Markdown("Set checkbox color using the `color` prop.")),
        OnlyComponentBlock(
            [
                dmc.Group(
                    position="apart",
                    children=[
                        dmc.Checkbox(
                            id="checkbox-color",
                            label="Use me as a boolean input",
                            checked=True,
                            color="green",
                        ),
                        dmc.Select(
                            id="color-checkbox-demo",
                            value="green",
                            searchable=False,
                            clearable=False,
                            data=[
                                {
                                    "label": val.title(),
                                    "value": val,
                                }
                                for val in [
                                    "dark",
                                    "gray",
                                    "red",
                                    "pink",
                                    "grape",
                                    "violet",
                                    "indigo",
                                    "blue",
                                    "cyan",
                                    "teal",
                                    "green",
                                    "lime",
                                    "yellow",
                                    "orange",
                                ]
                            ],
                        ),
                    ],
                )
            ]
        ),
        dmc.Space(h=40),
        ComponentReference(apidocs),
    ]
)

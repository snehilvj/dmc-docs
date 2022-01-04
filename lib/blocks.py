from pathlib import Path

import dash_mantine_components as dmc
from dash import html, dcc

from data import data
from lib.parser import get_component_reference, load_example


def ComponentName(string, **kwargs):
    return dmc.Text(string, style={"fontSize": 40, "fontWeight": 300}, **kwargs)


def Heading(string, **kwargs):
    return dmc.Title(string, order=5, style={"marginBottom": 10}, **kwargs)


def Text(string, **kwargs):
    return dmc.Text(
        dcc.Markdown(string), color="gray", style={"marginBottom": 20}, **kwargs
    )


def ComponentReference(component_name):
    docs = get_component_reference(component_name)
    return html.Div(
        [
            Heading("Keyword Arguments"),
            dmc.Prism(code=docs, language="git", style={"marginBottom": 50}),
        ]
    )


def CodeBlock(file, example_name, app, run=True, prism=True):
    path = Path(file).parent.joinpath("examples", example_name)
    component, source = load_example(path, app, run)
    return html.Div(
        [
            (
                dmc.Paper(
                    component,
                    withBorder=True,
                    padding="xl",
                    style={"marginBottom": 10},
                )
                if run
                else None
            ),
            (dmc.Prism(code=source, language="python") if prism else None),
            dmc.Space(h=40),
        ]
    )


def DocsBlock(component_name, children):
    sidebar_elements = [
        dmc.Anchor(component, href=f"/{component.lower()}")
        if component != component_name
        else dmc.Text(component, color="gray")
        for component in data
    ]

    return dmc.Container(
        fluid=True,
        padding="lg",
        style={"marginTop": 80},
        children=[
            dcc.Location(id="url"),
            dmc.Header(
                height=70,
                fixed=True,
                padding="md",
                children=[
                    dmc.Group(
                        position="apart",
                        style={"paddingTop": 1, "marginLeft": 20, "marginRight": 20},
                        children=[
                            dmc.Anchor(
                                "Dash Mantine Components", variant="gradient", size="xl"
                            ),
                            dmc.Group(
                                [
                                    dmc.Select(
                                        id="select-component",
                                        style={"width": 300},
                                        placeholder="Search for component",
                                        nothingFound="No match found",
                                        data=[
                                            {
                                                "label": component,
                                                "value": f"/{component.lower()}",
                                            }
                                            for component in data
                                        ],
                                    ),
                                    html.A(
                                        html.I(
                                            className="bi bi-github",
                                            style={"fontSize": 30, "color": "black"},
                                        ),
                                        href="https://github.com/snehilvj/dash-mantine-components",
                                    ),
                                ]
                            ),
                        ],
                    )
                ],
            ),
            dmc.Navbar(
                position="left",
                fixed=True,
                width={"base": 300},
                style={"top": 70},
                children=[
                    dmc.ScrollArea(
                        style={"height": "calc(100% - 70px)"},
                        offsetScrollbars=True,
                        children=[
                            dmc.Accordion(
                                state={"0": True},
                                iconPosition="right",
                                children=[
                                    dmc.AccordionItem(
                                        label="Getting Started",
                                        children=[
                                            dmc.Group(
                                                direction="column",
                                                spacing="xs",
                                                children=[
                                                    dmc.Anchor(
                                                        "Installation", href="/"
                                                    ),
                                                ],
                                            )
                                        ],
                                    )
                                ],
                            ),
                            dmc.Accordion(
                                state={"0": True},
                                iconPosition="right",
                                children=[
                                    dmc.AccordionItem(
                                        label="Components",
                                        children=[
                                            dmc.Group(
                                                direction="column",
                                                spacing="xs",
                                                children=sidebar_elements,
                                            )
                                        ],
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            ),
            html.Div(
                style={"marginLeft": 340, "marginRight": 20},
                children=[
                    ComponentName(component_name),
                    *children,
                    ComponentReference(component_name),
                ],
            ),
        ],
    )

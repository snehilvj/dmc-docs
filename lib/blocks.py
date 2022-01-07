from pathlib import Path

import dash_mantine_components as dmc
from dash import html, dcc

from data import component_list
from lib.parser import get_component_reference, load_example


def ComponentName(string, **kwargs):
    return dmc.Text(string, style={"fontSize": 40, "fontWeight": 300}, **kwargs)


def Heading(string, id, **kwargs):
    return dmc.Title(
        string, order=5, class_name="toc", id=id, style={"marginBottom": 10}, **kwargs
    )


def Text(string, **kwargs):
    return dmc.Text(
        dcc.Markdown(string), color="gray", style={"marginBottom": 20}, **kwargs
    )


def ComponentDescription(string, **kwargs):
    return dmc.Text(
        dcc.Markdown(string),
        color="gray",
        style={
            "marginBottom": 25,
            "marginTop": -15,
            "fontSize": 18,
        },
        **kwargs,
    )


def ComponentReference(component_name):
    docs = get_component_reference(component_name)
    return html.Div(
        [
            Heading("Keyword Arguments", id="keyword-arguments"),
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


def MantineThemeColorSwatches(id):
    return dmc.ColorPicker(
        id=id,
        value="#228ae6",
        withPicker=False,
        swatchesPerRow=7,
        swatches=[
            "#25262b",
            "#868e96",
            "#fa5252",
            "#e64980",
            "#be4bdb",
            "#7950f2",
            "#4c6ef5",
            "#228ae6",
            "#15abbf",
            "#12b886",
            "#3fbf57",
            "#82c91e",
            "#fab005",
            "#fc7d14",
        ],
    )


def DemoSlider(id, label, initial_value):
    return dmc.InputWrapper(
        label=label,
        children=[
            html.Div(
                [
                    dmc.Slider(
                        id=id,
                        drag_value=initial_value,
                        value=initial_value,
                        marks=[
                            {"value": 1},
                            {"value": 2},
                            {"value": 3},
                            {"value": 4},
                            {"value": 5},
                        ],
                        min=1,
                        max=5,
                        size="sm",
                        label="""(value) => window.sizeMap[value]""",
                    )
                ],
                style={"padding": "0 5px"},
            )
        ],
    )


def DemoSelect(id, value, label, data):
    return dmc.Select(
        id=id,
        value=value,
        label=label,
        searchable=False,
        clearable=False,
        data=[
            {
                "label": val.title(),
                "value": val,
            }
            for val in data
        ],
    )


def PageHeader():
    return dmc.Header(
        height=70,
        fixed=True,
        padding="md",
        children=[
            dmc.Group(
                position="apart",
                style={"paddingTop": 1, "marginLeft": 20, "marginRight": 20},
                children=[
                    dmc.Anchor(
                        "Dash Mantine Components",
                        variant="gradient",
                        size="xl",
                        href="/",
                    ),
                    dmc.Group(
                        id="header-right-section",
                        children=[
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
                                    for component in component_list
                                ],
                            ),
                            html.A(
                                html.I(
                                    className="bi bi-github",
                                    style={"fontSize": 30, "color": "black"},
                                ),
                                href="https://github.com/snehilvj/dash-mantine-components",
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def SideNav():
    sidebar_elements = [
        dmc.Anchor(component, size="sm", href=f"/{component.lower()}")
        for component in component_list
    ]

    return dmc.Navbar(
        id="components-navbar",
        fixed=True,
        position={"top": 70},
        width={"base": 250},
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
                                                "Installation",
                                                href="/installation",
                                                size="sm",
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
    )


def TableOfContents(children, title):
    toc = []
    for child in children:
        if isinstance(child, dmc.Title) and child.class_name == "toc":
            toc.append(
                dmc.Anchor(
                    child.children,
                    style={"text-transform": "capitalize"},
                    href=f"#{child.id}",
                    size="sm",
                )
            )

    if title in component_list:
        toc.append(
            dmc.Anchor("Keyword Arguments", href="#keyword-arguments", size="sm")
        )

    return dmc.Navbar(
        id="toc-navbar",
        position={"top": 90, "right": 0},
        fixed=True,
        width={"base": 280},
        style={"paddingRight": 30},
        children=[
            dmc.Text("Table of Contents", style={"marginBottom": 20}, weight=500),
            dmc.Group(direction="column", spacing="xs", children=toc),
        ],
    )


def PageBlock(title, children):
    children = [ComponentName(title)] + children

    return dmc.Container(
        fluid=True,
        padding="lg",
        style={"marginTop": 90},
        children=[
            dcc.Location(id="url"),
            PageHeader(),
            SideNav(),
            dmc.Container(
                padding="lg",
                id="main-content",
                children=children,
            ),
            TableOfContents(children, title),
        ],
    )


def DocsBlock(component_name, children):
    children.append(ComponentReference(component_name))
    return PageBlock(component_name, children)

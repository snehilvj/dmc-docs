from pathlib import Path

import dash_mantine_components as dmc
from dash import dcc

from lib.parser import load_example


def IntroBlock(text):
    title, descr = text.split("|")

    layout = [
        dmc.Text(title, style={"fontSize": 40, "fontWeight": 300}),
        dmc.Text(
            dcc.Markdown(descr),
            color="gray",
            style={
                "marginBottom": 25,
                "marginTop": -15,
                "fontSize": 18,
            },
        ),
    ]

    return layout


def Heading(text, id):
    return dmc.Title(
        text,
        order=5,
        id=id,
        style={"marginBottom": 10, "marginTop": 30, "text-transform": "capitalize"},
    )


def Paragraph(text):
    return dmc.Text(
        dcc.Markdown(text), color="gray", style={"marginBottom": 20, "marginTop": -10}
    )


def DmcCodeBlock(file):
    component, _ = load_example(file)
    return component


def ExecCodeBlock(file, run, prism):
    component, source = load_example(file, run)

    layout = [
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
        (
            dmc.Prism(source, language="python", style={"marginBottom": 50})
            if prism
            else None
        ),
    ]

    return layout


def SnippetBlock(file, language):
    path = Path.cwd().joinpath("pages", file)
    source = path.read_text()
    return dmc.Prism(source, language=language, style={"marginBottom": 50})


def ApiDoc(component):
    comp = getattr(dmc, component)
    component_doc = comp.__doc__
    docs = component_doc.split("Keyword arguments:")[-1]
    docs = docs.lstrip("\n\n")

    return [
        Heading("Keyword Arguments", id="keyword-arguments"),
        dmc.Prism(docs, language="git", style={"marginBottom": 50}, noCopy=True),
    ]


def TableOfContents(toc):
    children = []
    for content in toc:
        children.append(
            dmc.Anchor(
                content["text"],
                style={"text-transform": "capitalize", "textDecoration": "none"},
                href=f"#{content['id']}",
                size="sm",
            )
        )

    return dmc.Navbar(
        id="toc-navbar",
        position={"top": 90, "right": 0},
        fixed=True,
        width={"base": 280},
        style={"paddingRight": 20},
        children=[
            dmc.Text("Table of Contents", style={"marginBottom": 10}, weight=500),
            dmc.Group(direction="column", spacing=0, children=children),
        ],
    )

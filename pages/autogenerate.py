import os
from pathlib import Path
from typing import Optional

import dash
import dash_mantine_components as dmc
import frontmatter
from dash_iconify import DashIconify
from mistune.directives import extract_toc_items
from pydantic import BaseModel

from lib.appshell import create_table_of_contents
from lib.renderer import markdown
from lib.utils import create_styles_api_table


# front matter model
class Meta(BaseModel):
    name: str
    section: str
    head: str
    description: str
    component: Optional[str]
    dmc: bool = True
    props: bool = True
    styles: str = ""
    category: str = "core"


directory = "docs"
# read all markdown files
files = Path(directory).glob("**/*.md")


def make_endpoint(name):
    return "-".join(name.lower().split())


def create_kwargs(component):
    if component == "DashIconify":
        component_doc = DashIconify.__doc__
    else:
        comp = getattr(dmc, component)
        component_doc = comp.__doc__
    docs = component_doc.split("Keyword arguments:")[-1]
    kwargs = dmc.Prism(docs, language="git", noCopy=True)
    heading = markdown.parse(f"###### {component}")
    heading.append(kwargs)
    return heading


for file in files:
    contents = file.read_text()
    # extract front matter
    matter, rem = frontmatter.parse(contents)
    # validate meta
    meta = Meta(**matter)

    headers = []
    docs_tab = []
    kwargs_tab = [dmc.Space(h=20)]
    styles_tab = [dmc.Space(h=20)]

    # add title
    title = dmc.Text(meta.name, style={"fontSize": 30, "fontWeight": 300})
    headers.append(title)

    # add head
    head = dmc.Text(meta.head, mb=25)
    headers.append(head)

    # render markdown into dmc components
    docs_page = markdown.parse(rem)
    docs_tab.extend(docs_page)

    # add keyword arguments section
    if meta.component:
        if meta.props:
            kwargs_tab.extend(
                markdown.parse(
                    """Along with the props mentioned below, these dmc components also Mantine style props such as 
                    `m`, `mx`, `my`, `p`, etc. Click [here](/style-props) for more information. """
                )
            )
        comps = meta.component.split(", ")
        for comp in comps:
            section = create_kwargs(comp)
            kwargs_tab.extend(section)

    # extract and append TOC
    toc_items = extract_toc_items(markdown, rem)
    toc = create_table_of_contents(toc_items)
    docs_tab.append(toc)

    path_prefix = "/components/" if meta.dmc else "/"

    if meta.styles and os.environ.get("LOAD_STYLES"):
        styles_tab.extend(create_styles_api_table(meta.category, meta.styles))
        styles_tab.append(
            dmc.Anchor(
                "Click here for more information on using the styles API.",
                href="/styles-api",
            )
        )

    layout = (
        [
            *headers,
            dmc.Tabs(
                [
                    dmc.TabsList(
                        [
                            dmc.Tab("Documentation", value="docs"),
                            dmc.Tab("Component Props", value="props"),
                            dmc.Tab("Styles API", value="styles")
                            if meta.styles
                            else None,
                        ]
                    ),
                    dmc.TabsPanel(docs_tab, value="docs"),
                    dmc.TabsPanel(kwargs_tab, value="props"),
                    dmc.TabsPanel(styles_tab, value="styles") if meta.styles else None,
                ],
                value="docs",
                variant="outline",
                mt=40,
                mb=50,
            ),
        ]
        if meta.component
        else headers + docs_tab + [dmc.Space(h=50)]
    )

    # register with dash
    dash.register_page(
        meta.name,
        path_prefix + make_endpoint(meta.name),
        name=meta.name,
        title="Dash Mantine Components - " + meta.name,
        description=meta.description,
        section=meta.section,
        layout=layout,
    )

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


# front matter model
class Meta(BaseModel):
    name: str
    section: str
    head: str
    description: str
    component: Optional[str]


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
    docs = docs.lstrip("\n\n")
    kwargs = dmc.Prism(docs, language="git", noCopy=True)
    heading = markdown.parse("##### Keyword Arguments")
    heading.append(kwargs)
    return heading


for file in files:
    contents = file.read_text()
    # extract front matter
    matter, rem = frontmatter.parse(contents)
    # validate meta
    meta = Meta(**matter)

    layout = []

    # add title
    title = dmc.Text(meta.name, style={"fontSize": 30, "fontWeight": 300})
    layout.append(title)

    # add head
    head = dmc.Text(
        meta.head,
        color="gray",
        style={
            "marginBottom": 25,
        },
    )
    layout.append(head)

    # render markdown into dmc components
    docs_page = markdown.parse(rem)
    layout.extend(docs_page)

    # add keyword arguments section
    if meta.component:
        section = create_kwargs(meta.component)
        layout.extend(section)

    # extract and append TOC
    toc_items = extract_toc_items(markdown, rem)
    if meta.component:
        toc_items.append(("#keyword-arguments", "Keyword Arguments", ""))
    toc = create_table_of_contents(toc_items)
    layout.append(toc)

    # add space
    layout.append(dmc.Space(h=50))

    path_prefix = "/components/" if meta.component else "/"

    # register with dash
    dash.register_page(
        meta.name,
        path_prefix + make_endpoint(meta.name),
        name=meta.name,
        title="Dash Mantine Components - " + meta.name,
        section=meta.section,
        layout=layout,
    )

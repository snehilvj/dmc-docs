from pathlib import Path
from typing import Optional

import dash
import dash_mantine_components as dmc
import frontmatter
from dash_iconify import DashIconify
from mistune.directives import extract_toc_items
from pydantic import BaseModel

from lib.appshell import create_table_of_contents
from lib.propdef import propdefs_to_exclude
from lib.renderer import markdown


# front matter model
class Meta(BaseModel):
    name: str
    section: str
    head: str
    description: str
    component: Optional[str]
    dmc: bool = True


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
    for to_replace in propdefs_to_exclude.split("\n"):
        docs = docs.replace(to_replace, "")
    lines = docs.split("\n")
    new = []
    for line in lines:
        if not line:
            continue
        if line.startswith("- ") and line.endswith("):"):
            line = "\n" + line
        new.append(line)
    docs = "\n".join(new)
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
        layout.extend(markdown.parse("##### Keyword Arguments"))
        if meta.dmc:
            layout.extend(
                markdown.parse(
                    """Along with the props mentioned below, all dmc components also support margin and padding props 
                    such as `m`, `mx`, `my`, `p`, `pb`, `pt`, etc. """
                )
            )
        comps = meta.component.split(", ")
        for comp in comps:
            section = create_kwargs(comp)
            layout.extend(section)

    # extract and append TOC
    toc_items = extract_toc_items(markdown, rem)
    if meta.component:
        toc_items.append(("#keyword-arguments", "Keyword Arguments", ""))
    toc = create_table_of_contents(toc_items)
    layout.append(toc)

    # add space
    layout.append(dmc.Space(h=50))

    path_prefix = "/components/" if meta.dmc else "/"

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

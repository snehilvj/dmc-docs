from pathlib import Path

import dash
import dash_mantine_components
import frontmatter
from markdown2dash import Admonition, BlockExec, Image
from markdown2dash import parse
from pydantic import BaseModel

from components.kwargs import Kwargs
from components.toc import TableOfContents
from lib.constants import PAGE_TITLE_PREFIX

directory = "docs"

# read all markdown files
files = Path(directory).glob("**/*.md")


class Meta(BaseModel):
    name: str
    description: str
    endpoint: str
    package: str = "dash_mantine_components"


def make_endpoint(name):
    return "-".join(name.lower().split())


for file in files:
    metadata, content = frontmatter.parse(file.read_text())
    metadata = Meta(**metadata)

    layout = parse(
        content,
        directives=[Admonition(), Kwargs(), BlockExec(), TableOfContents(), Image()],
    )

    # register with dash
    dash.register_page(
        metadata.name,
        metadata.endpoint,
        name=metadata.name,
        title=PAGE_TITLE_PREFIX + metadata.name,
        description=metadata.description,
        layout=layout,
    )

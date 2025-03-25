import logging
from pathlib import Path
from typing import Optional

import dash
import dash_mantine_components as dmc
import frontmatter
from markdown2dash import Admonition, BlockExec, Divider, Image, create_parser
from pydantic import BaseModel

from lib.constants import PAGE_TITLE_PREFIX
from lib.directives.kwargs import Kwargs
from lib.directives.source import SC
from lib.directives.toc import TOC
from lib.directives.styles_api_text import StylesApiText

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

directory = "docs"

# read all markdown files
files = Path(directory).glob("**/*.md")


class Meta(BaseModel):
    name: str
    description: str
    endpoint: str
    package: str = "dash_mantine_components"
    category: Optional[str] = None
    order: Optional[int] = None


def make_endpoint(name):
    return "-".join(name.lower().split())


directives = [Admonition(), BlockExec(), Divider(), Image(), Kwargs(), SC(), TOC(), StylesApiText()]
parse = create_parser(directives)

for file in files:
    logger.info("Loading %s..", file)
    metadata, content = frontmatter.parse(file.read_text())
    metadata = Meta(**metadata)
    layout = parse(content)

    # add heading and description to the layout
    section = [
        dmc.Title(metadata.name, order=2, className="m2d-heading"),
        dmc.Text(metadata.description, className="m2d-paragraph"),
    ]
    layout = section + layout

    # register with dash
    dash.register_page(
        metadata.name,
        metadata.endpoint,
        name=metadata.name,
        title=PAGE_TITLE_PREFIX + metadata.name,
        description=metadata.description,
        layout=layout,
        category=metadata.category,
        order=metadata.order
    )

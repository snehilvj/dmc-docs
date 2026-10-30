import logging
from pathlib import Path
from typing import Optional

import dash
import dash_mantine_components as dmc
import frontmatter
from markdown2dash import Admonition, BlockExec, Divider, Image, create_parser
from pydantic import BaseModel

from utils.constants import PAGE_TITLE_SUFFIX
from utils.directives.functions_as_props import FunctionsAsProps
from utils.directives.kwargs import Kwargs
from utils.directives.source import SC
from utils.directives.toc import TOC
from utils.directives.styles_api_text import StylesApiText
from utils.directives.llms_copy import LlmsCopy
from utils.directives.style_props_text import StylePropsText
from utils.directives.execv3 import Exec3

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


directives = [Admonition(), BlockExec(), Divider(), Image(), Kwargs(), SC(), TOC(), StylesApiText(), FunctionsAsProps(), LlmsCopy(), StylePropsText(), Exec3()]
parse = create_parser(directives)

for file in files:
    logger.info("Loading %s..", file)
    metadata, content = frontmatter.parse(file.read_text(encoding="utf-8"))
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
        title=metadata.name + PAGE_TITLE_SUFFIX,
        description=metadata.description,
        layout=layout,
        category=metadata.category,
        order=metadata.order
    )

logger.info("""
********************************
To update llms.txt and llms.json:

From the llm directory, run:
    python generate_llms_text.py
********************************
""")
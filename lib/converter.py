from dash import html

from lib.blocks import (
    IntroBlock,
    Heading,
    Paragraph,
    ApiDoc,
    DmcCodeBlock,
    ExecCodeBlock,
    TableOfContents,
    SnippetBlock,
)
from lib.renderer import markdown
from pathlib import Path

component_map = {
    "heading": Heading,
    "paragraph": Paragraph,
    "apidoc": ApiDoc,
    "dmc": DmcCodeBlock,
    "example": ExecCodeBlock,
    "snippet": SnippetBlock,
}


def convert_md_to_dash_layout(file, is_component=True):
    path = Path.cwd().joinpath("pages", file)
    raw = path.read_text()
    text = markdown(raw)
    toc = []
    layout = []
    layout.extend(IntroBlock(text[0]["text"]))

    for block in text[1:]:
        name = block.pop("block-name")
        if name == "heading":
            toc.append(block)

        layout_block = component_map[name](**block)
        if not isinstance(layout_block, list):
            layout_block = [layout_block]

        layout.extend(layout_block)

    if is_component:
        toc.append({"text": "Keyword Arguments", "id": "keyword-arguments"})

    layout.append(TableOfContents(toc))

    return html.Div(children=layout)

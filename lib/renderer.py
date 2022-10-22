from urllib.parse import urlparse

import dash_mantine_components as dmc
import mistune
from dash import html
from mistune import AstRenderer, create_markdown
from mistune.directives import DirectiveToc

from lib.directives import ExecBlock, GalleryBlock, Admonition


def toc_plugin_patch(text, level, state):
    tid = "-".join(text.lower().split())
    state["toc_headings"].append(("#" + tid, text, level))
    return {"type": "theading", "text": text, "params": (level, tid)}


# patch work
mistune.directives.toc.record_toc_heading = toc_plugin_patch


# noinspection PyMethodMayBeStatic
class DmcRenderer(AstRenderer):
    def theading(self, children, level, tid):
        text = children[0]
        return dmc.Title(text, order=level, id=tid, className="renderer-title")

    def thematic_break(self):
        return dmc.Divider()

    def block_quote(self, text):
        return dmc.Blockquote(text[0].children, className="renderer-quote")

    def block_code(self, children, info=None):
        return dmc.Prism(children, language=info, className="renderer-code")

    def newline(self):
        return

    def table(self, text):
        return dmc.Group(
            dmc.Paper(dmc.Table(text, highlightOnHover=True), withBorder=True),
            className="renderer-table",
            position="center",
        )

    def table_head(self, text):
        return html.Thead(html.Tr(text))

    def table_body(self, text):
        return html.Tbody(text)

    def table_row(self, text):
        return html.Tr(text)

    def table_cell(self, text, align=None, is_head=False):
        return html.Th(text) if is_head else html.Td(text)

    def paragraph(self, text):
        return dmc.Text(text, style={"fontSize": 15}, className="renderer-text")

    def text(self, text):
        return text

    def block_text(self, text):
        return text

    def link(self, link, children=None, title=None):
        return dmc.Anchor(
            children[0],
            href=link,
            target="_blank" if bool(urlparse(link).netloc) else "_self",
            underline=False,
            style={"fontSize": 15},
            className="renderer-anchor",
        )

    def codespan(self, text):
        return dmc.Code(text, color="orange")

    def list(self, children, ordered, level, start=None):
        return dmc.List(
            children,
            type="ordered" if ordered else "unordered",
            spacing=5,
            size="sm",
            withPadding=True,
            className="renderer-list",
        )

    def list_item(self, text, level):
        if isinstance(text[0], list):
            children = text[0]
        else:
            children = text[0].children
        return dmc.ListItem(dmc.Text(children))


markdown = create_markdown(
    renderer=DmcRenderer(),
    plugins=["table", ExecBlock(), Admonition(), GalleryBlock(), DirectiveToc()],
)

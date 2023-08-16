import dash_mantine_components as dmc
from dash import html
from dash.development.base_component import Component

from markdown2dash import TableOfContents as TOC


class TableOfContents(TOC):
    def render(self, renderer, title: str, content: str, **options) -> Component:
        table_of_contents = options.pop("table_of_contents")
        paddings = {3: 0, 4: 20, 5: 40}
        links = [
            html.A(
                dmc.Text(text, color="dimmed", size="sm", variant="text"),
                href="#" + hid,
                style={
                    "textTransform": "capitalize",
                    "textDecoration": "none",
                    "paddingLeft": paddings[level],
                    "width": "fit-content",
                },
            )
            for level, text, hid in table_of_contents
            if level >= 3
        ]

        heading = dmc.Text(title, mb=10, weight=500) if links else None
        content = dmc.Stack([heading, *links], spacing=6, px=25, mt=20)

        return dmc.Aside(
            position={"top": 70, "right": 0},
            fixed=True,
            id="toc-navbar",
            width={"base": 300},
            zIndex=10,
            children=content,
            withBorder=False,
        )

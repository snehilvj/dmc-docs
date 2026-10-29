import dash_mantine_components as dmc
from dash import html
from dash.development.base_component import Component

from markdown2dash import TableOfContents


class TOC(TableOfContents):
    def render(self, renderer, title: str, content: str, **options) -> Component:
        table_of_contents = options.pop("table_of_contents")
        paddings = {3: 0, 4: 20, 5: 40}
        links = [
            html.A(
                dmc.Text(text, c="dimmed", size="sm", variant="text"),
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

        heading = dmc.Text(title, mb=10, fw=500) if links else None

        ad = dmc.Box(
            **{
                "data-ea-publisher": "dash-mantine-componentscom",
                "data-ea-manual": True,
                "data-ea-type": "text",
                "className": "flat",
                "id": "ethical-ads-box",
            },
            my=25,
            ml=-15
        )

        content = dmc.Stack([ad, heading, *links, dmc.Space(h=20)], gap=6, px=25)
        return dmc.AppShellAside(
            children=dmc.ScrollArea(content, type="never"), withBorder=False
        )



import dash_mantine_components as dmc
from dash import  dcc, html
from dash.development.base_component import Component
from markdown2dash import BaseDirective
from lib.constants import LLMS


class LlmsCopy(BaseDirective):
    NAME = "llms_copy"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        llm_content = next((i["content"] for i in LLMS if i["name"] == title), None)
        if llm_content is None:
            print(f"Unable to find {title} in llms.json")

        component = dmc.Box([
            html.Label(
                "Copy for llm",
                id="copy-label",
                style={"cursor": "pointer", "marginRight": 5}
            ),
            dcc.Clipboard(
                id="clipboard-target",
                content=llm_content,
                style={"display": "inline-block", "cursor": "pointer"}

            )
        ], id="clipboard-wrapper", c="dimmed", my="md")

        return component
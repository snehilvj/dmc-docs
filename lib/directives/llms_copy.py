import textwrap
import dash_mantine_components as dmc
from dash import  dcc, html
from dash.development.base_component import Component
from markdown2dash import BaseDirective
from lib.constants import NAME_CONTENT_MAP, DMC_VERSION


class LlmsCopy(BaseDirective):
    NAME = "llms_copy"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        llm_content = NAME_CONTENT_MAP.get(title, "")


        llm_intro = textwrap.dedent(f"""
        > Dash Mantine Components v{DMC_VERSION} Documentation for {title}
        > See complete docs at https://www.dash-mantine-components.com/assets/llms.txt  
        > All relative links in this file should be resolved against https://www.dash-mantine-components.com
        
        """)


        if llm_content is None:
            print(f"Unable to find {title} in llms.json")

        component = dmc.Box([
            dmc.Box([
                html.Label(
                    "Copy for llm",
                    id="copy-label",
                    style={"cursor": "pointer", "marginRight": 5}
                ),
                dcc.Clipboard(
                    id="clipboard-target",
                    content=llm_intro + llm_content,
                    style={"display": "inline-block", "cursor": "pointer"}

                )
            ], id="clipboard-wrapper", c="dimmed", my="md", display="inline-block"),
            dmc.Tooltip(target="#clipboard-wrapper", label="Copy page as markdown for LLMs")
        ], display="inline-blick")

        return component
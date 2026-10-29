
import dash_mantine_components as dmc
from dash.development.base_component import Component
from markdown2dash import BaseDirective


class StylesApiText(BaseDirective):
    NAME = "styles_api_text"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        component = dmc.Box([
            dmc.Text("This component supports the ", span=True),
            dmc.Anchor("Styles API", href="/styles-api"),
            dmc.Text("""
            allowing you to customize the styles of any inner element.  
            
            """, span=True),
        ], mb="sm")
        return component

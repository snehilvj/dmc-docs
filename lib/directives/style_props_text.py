import dash_mantine_components as dmc
from dash.development.base_component import Component
from markdown2dash import BaseDirective


class StylePropsText(BaseDirective):
    NAME = "style_props_text"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        component = dmc.Box(
            [
                dmc.Text("This component also supports style props.  See the ", span=True),
                dmc.Anchor("Style Props guide", href="/style-props"),
                dmc.Text(" for more information.", span=True),
            ]
        )
        return component



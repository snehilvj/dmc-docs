

import dash_mantine_components as dmc
from dash.development.base_component import Component
from markdown2dash import BaseDirective


class FunctionsAsProps(BaseDirective):
    NAME = "functions_as_props"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        component = dmc.Box([
            dmc.Text("Note: This example uses custom JavaScript defined in the assets folder. Learn more at ", span=True),
            dmc.Anchor("Functions As Props", href="/functions-as-props"),
        ], mb="lg")
        return component

import importlib
import inspect

import dash_mantine_components as dmc
from dash.development.base_component import Component
from markdown2dash import BaseDirective

class Exec3(BaseDirective):

    NAME = "exec3"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        code = options.pop("code", "true")
        border = options.pop("border", "true")
        defaultExpanded = options.pop("defaultExpanded", "false")
        withExpandedButton = options.pop("withExpandedButton", "true")
        display = options.pop("display", "block")
        maxCollapsedHeight = options.pop("maxCollapsedHeight","200px"),

        imported = importlib.import_module(title)
        components = [
            dmc.Paper(
                getattr(imported, "component"), withBorder=border == "true", p="xl"
            )
        ]
        if code == "true":
            source = inspect.getsource(imported).replace("component = ", "", 1)
            prism = dmc.CodeHighlight(
                source,
                language="python",
                defaultExpanded=defaultExpanded == "true",
                withExpandButton=withExpandedButton == 'true',
                maxCollapsedHeight=maxCollapsedHeight,
                display=display,
            )
            components.append(prism)
        return dmc.Box(components, **options)
#
# """
# sample usage:
#
# options for CodeHightlight available in v3 such as defaultExpanded
# use :display: "none" to include in llms.txt but not shown in docs
#
#
# .. exex3::docs.alert.auto
#     :defaultExpanded: false
#     :withExpandedButton: true
#     :maxCollapsedHeight: "325px"
#     :display: none
#
# """

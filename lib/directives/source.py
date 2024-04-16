import os

import dash_mantine_components as dmc
from dash.development.base_component import Component
from dash_iconify import DashIconify
from markdown2dash import SourceCode


class SC(SourceCode):
    NAME = "source"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        mapping = {
            "py": {"language": "python", "icon": DashIconify(icon="devicon:python")},
            "css": {"language": "css", "icon": DashIconify(icon="devicon:css3")},
        }
        files = title.split(", ")
        code = []
        for file in files:
            extension = file.split(".")[-1]
            code.append(
                {
                    "fileName": os.path.basename(file),
                    "code": open(file, "r").read(),
                    "language": mapping[extension]["language"],
                    "icon": mapping[extension]["icon"],
                }
            )
        return dmc.CodeHighlightTabs(code=code)

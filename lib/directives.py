import importlib
from pathlib import Path

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
from mistune.directives import Directive


def create_prism(file):
    source = Path(file).read_text()
    source = source.replace("component = ", "", 1)
    return dmc.Prism(source, language="python")


class BaseDirective(Directive):
    directive_name: str

    def __call__(self, md):
        self.register_directive(md, self.directive_name)
        md.renderer.register(self.directive_name, lambda raw: self.render(**raw))

    def parse(self, block, m, state):
        raise NotImplementedError()

    def render(self, **kwargs):
        raise NotImplementedError()


class ExecCodeBlock(BaseDirective):
    directive_name = "exec-block"

    def parse(self, block, m, state):
        value = m.group("value")
        options = self.parse_options(m)
        options = {item[0]: item[1] for item in options}
        return {
            "type": self.directive_name,
            "raw": {"module": value, "prism": options.get("prism", "true")},
        }

    def render(self, module, prism):
        imported = importlib.import_module(module)
        components = [
            dmc.Paper(getattr(imported, "component"), withBorder=True, p="xl")
        ]
        if prism == "true":
            source = create_prism(imported.__file__)
            source.style = {"marginTop": 10}
            components.append(source)
        return html.Div(components, style={"marginBottom": 10})


class GalleryBlock(BaseDirective):
    directive_name = "gallery-block"

    def parse(self, block, m, state):
        value = m.group("value")
        options = self.parse_options(m)
        options = {item[0]: item[1] for item in options}
        return {
            "type": self.directive_name,
            "raw": {
                "module": value,
                "label": options["label"],
                "center": options.get("center", "true"),
            },
        }

    def render(self, module, label, center):
        imported = importlib.import_module(module)
        component = getattr(imported, "component")
        if center == "true":
            component = dmc.Center(component)

        tab1 = dmc.Tab(
            dmc.Paper(component, withBorder=True, p="xl"),
            label=label,
            icon=[DashIconify(icon="radix-icons:enter")],
        )
        source = create_prism(imported.__file__)
        tab2 = dmc.Tab(
            source, label="Code", icon=[DashIconify(icon="radix-icons:code")]
        )
        return dmc.Tabs(
            [tab1, tab2], variant="outline", style={"marginBottom": 20, "marginTop": 20}
        )


class Admonition(BaseDirective):
    directive_name = "admonition"

    def parse(self, block, m, state):
        value = m.group("value")
        text = self.parse_text(m)
        options = self.parse_options(m)
        options = {item[0]: item[1] for item in options}
        return {
            "type": self.directive_name,
            "raw": {
                "title": value,
                "text": text,
                "icon": options.get("icon"),
                "color": options.get("color", "true"),
            },
        }

    def render(self, title, text, icon, color):
        return dmc.Alert(
            title=title, children=text, icon=[DashIconify(icon=icon)], color=color, style={"marginBottom": 10}
        )

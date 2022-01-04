from dash import Dash
from flask import Blueprint, render_template


class DmcDash(Dash, Blueprint):
    def __init__(self, import_name, endpoint, **kwargs):
        Blueprint.__init__(self, endpoint, import_name, url_prefix=f"/{endpoint}")
        kwargs["url_base_pathname"] = f"/{endpoint}/"
        kwargs["name"] = import_name
        kwargs["server"] = False
        super().__init__(**kwargs)

    def index(self, *args, **kwargs):
        return render_template(
            "docs.html",
            css=self._generate_css_dist_html(),
            config=self._generate_config_html(),
            scripts=self._generate_scripts_html(),
            meta=self._generate_meta_html(),
            renderer=self._generate_renderer(),
        )

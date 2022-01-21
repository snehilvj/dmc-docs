import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__)

layout = convert_md_to_dash_layout(
    "getting-started/installation/installation.md", is_component=False
)

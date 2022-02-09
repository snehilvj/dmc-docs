import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__, order=1)

layout = convert_md_to_dash_layout(
    "getting-started/installation/installation.md", is_component=False
)

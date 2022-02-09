import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__, name="DashIconify")

layout = convert_md_to_dash_layout("getting-started/dash-iconify/dash-iconify.md")

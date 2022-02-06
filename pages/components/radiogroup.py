import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__, name="RadioGroup")

layout = convert_md_to_dash_layout("components/radiogroup/radiogroup.md")

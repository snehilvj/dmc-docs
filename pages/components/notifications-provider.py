import dash

from lib.converter import convert_md_to_dash_layout

dash.register_page(__name__, name="Notifications Provider")

layout = convert_md_to_dash_layout(
    "components/notifications-provider/notifications-provider.md"
)

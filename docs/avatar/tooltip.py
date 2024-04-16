import dash_mantine_components as dmc
from dash import html

component = html.A(
    dmc.Tooltip(
        dmc.Avatar(
            src="https://e7.pngegg.com/pngimages/799/987/png-clipart-computer-icons-avatar-icon-design-avatar-heroes"
            "-computer-wallpaper-thumbnail.png",
            size="lg",
            radius="xl",
        ),
        label="Snehil Vijay",
        position="bottom",
    ),
    href="https://www.linkedin.com/in/snehilvj/",
    target="_blank",
)

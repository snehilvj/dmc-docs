import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Timeline(
    children=[
        dmc.TimelineItem(
            title="Default bullet",
            children=dmc.Text("Default bullet without anything", c="dimmed", size="sm")
        ),
        dmc.TimelineItem(
            title="Avatar",
            bullet=dmc.Avatar(
                size=22,
                radius="xl",
                src="https://avatars.githubusercontent.com/u/91216500?v=4"
            ),
            children=dmc.Text("Timeline bullet as avatar image", c="dimmed", size="sm")
        ),
        dmc.TimelineItem(
            title="Icon",
            bullet=DashIconify(icon="tabler:sun", width=13),
            children=dmc.Text("Timeline bullet as icon", c="dimmed", size="sm")
        ),
        dmc.TimelineItem(
            title="ThemeIcon",
            bullet=dmc.ThemeIcon(
                size=22,
                variant="gradient",
                gradient={"from": "lime", "to": "cyan"},
                radius="xl",
                children=DashIconify(icon="tabler:video", width=13)
            ),
            children=dmc.Text("Timeline bullet as ThemeIcon component", c="dimmed", size="sm")
        )
    ],
    bulletSize=24
)

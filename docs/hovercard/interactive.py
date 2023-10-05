import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = (
    dmc.HoverCard(
        shadow="md",
        children=[
            dmc.HoverCardTarget(
                dmc.Avatar(
                    src="https://avatars.githubusercontent.com/u/91216500?v=4",
                    radius="xl",
                )
            ),
            dmc.HoverCardDropdown(
                [
                    dmc.Text("Snehil Vijay"),
                    dmc.Group(
                        [
                            dmc.Anchor(
                                DashIconify(icon="openmoji:linkedin", width=40),
                                href="https://www.linkedin.com/in/snehilvj/",
                                target="_blank",
                            ),
                            dmc.Anchor(
                                DashIconify(icon="openmoji:github", width=40),
                                href="https://www.github.com/snehilvj/",
                                target="_blank",
                            ),
                            dmc.Anchor(
                                DashIconify(icon="openmoji:twitter", width=40),
                                href="https://twitter.com/snehilvj",
                                target="_blank",
                            ),
                        ],
                        p=0,
                    ),
                ]
            ),
        ],
    ),
)

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Timeline(
    [
        dmc.TimelineItem(
            title="New branch",
            bullet=DashIconify(icon="tabler:git-branch", width=12),
            opposite=dmc.Text("2 hours ago", size="sm", c="dimmed"),
            children=dmc.Text(
                [
                    "You've created new branch ",
                    dmc.Text("fix-notifications", variant="link", span=True, inherit=True),
                    " from master",
                ],
                c="dimmed",
                size="sm",
            ),
        ),
        dmc.TimelineItem(
            title="Commits",
            bullet=DashIconify(icon="tabler:git-commit", width=12),
            opposite=dmc.Text("52 minutes ago", size="sm", c="dimmed"),
            alternate=True,
            children=dmc.Text(
                [
                    "You've pushed 23 commits to ",
                    dmc.Text("fix-notifications branch", variant="link", span=True, inherit=True),
                ],
                c="dimmed",
                size="sm",
            ),
        ),
        dmc.TimelineItem(
            title="Pull request",
            bullet=DashIconify(icon="tabler:git-pull-request", width=12),
            lineVariant="dashed",
            opposite=dmc.Text("34 minutes ago", size="sm", c="dimmed"),
            children=dmc.Text(
                [
                    "You've submitted a pull request ",
                    dmc.Text(
                        "Fix incorrect notification message (#187)",
                        variant="link",
                        span=True,
                        inherit=True,
                    ),
                ],
                c="dimmed",
                size="sm",
            ),
        ),
        dmc.TimelineItem(
            title="Code review",
            bullet=DashIconify(icon="tabler:message-circle", width=12),
            opposite=dmc.Text("12 minutes ago", size="sm", c="dimmed"),
            alternate=True,
            children=dmc.Text(
                [
                    dmc.Text("Robert Gluesticker", variant="link", span=True, inherit=True),
                    " left a code review on your pull request",
                ],
                c="dimmed",
                size="sm",
            ),
        ),
    ],
    active=2,
    bulletSize=24,
    lineWidth=2,
)
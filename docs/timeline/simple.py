import dash_mantine_components as dmc


component = dmc.Timeline(
    [
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've created 'fix-notification' branch",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("2 hours ago", size="xs"),
            ],
            title="New Branch",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've pushed 23 commits to 'fix-notification' branch",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("42 minutes ago", size="xs"),
            ],
            title="Commits",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "You've submitted a pull request 'Fix incorrect notification message (#178)'",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("32 minutes ago", size="xs"),
            ],
            title="Pull Request",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    "Snehil left a comment on your pull request",
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text("12 minutes ago", size="xs"),
            ],
            title="Code Review",
        ),
    ],
    active=3,
)

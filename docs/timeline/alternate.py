import dash_mantine_components as dmc

component = dmc.Timeline(
    [
        dmc.TimelineItem(
            title="Project started",
            opposite=dmc.Text("Jan 2025", size="sm", c="dimmed"),
            children="Initial planning and requirements gathering.",
        ),
        dmc.TimelineItem(
            title="Beta release",
            opposite=dmc.Text("Apr 2025", size="sm", c="dimmed"),
            alternate=True,
            children="Released the first version to early adopters.",
        ),
        dmc.TimelineItem(
            title="General availability",
            opposite=dmc.Text("Aug 2025", size="sm", c="dimmed"),
            children="Launched publicly with full documentation.",
        ),
        dmc.TimelineItem(
            title="Version 2.0",
            opposite=dmc.Text("Jan 2026", size="sm", c="dimmed"),
            alternate=True,
            children="Introduced a redesigned interface and new features.",
        ),
    ],
    active=3,
    bulletSize=16,
    lineWidth=2,
)
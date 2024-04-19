import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Button("Hidden from sm", hiddenFrom="sm", color="orange"),
        dmc.Button("Visible from sm", visibleFrom="sm", color="cyan"),
        dmc.Button("Visible from md", visibleFrom="md", color="pink"),
    ],
    justify="center",
)

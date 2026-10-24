import dash_mantine_components as dmc

component = dmc.Tooltip(
    label="This tooltip stays open while you move the pointer onto it, so you can read or select its full contents without it closing.",
    interactive=True,
    withArrow=True,
    multiline=True,
    w=220,
    children=dmc.Button("Hover to read the tooltip"),
)
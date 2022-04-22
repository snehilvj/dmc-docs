import dash_mantine_components as dmc

component = dmc.TextInput(
    placeholder="Search",
    rightSectionWidth=80,
    rightSection=[dmc.Kbd("Ctrl + K")],
    style={"width": 400},
)

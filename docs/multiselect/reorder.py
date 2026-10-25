import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select your favorite superpowers",
    description="Drag pills to put them in order of preference.",
    data=["Teleport", "Time Travel", "Fly", "Invisibility", "Mind Reading"],
    value=["Teleport", "Time Travel", "Fly", "Invisibility", "Mind Reading"],
    withPillsReorder=True,
)
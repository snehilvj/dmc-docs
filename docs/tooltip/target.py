import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Button("Hover me to see tooltip", id="my-target"),
    dmc.Tooltip(target="#my-target", label="Tooltip over button")
])
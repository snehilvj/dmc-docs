import dash_mantine_components as dmc

component = dmc.Tooltip(
    dmc.Button("Button with tooltip"),
    label="Tooltip",
    events={"hover": False, "focus": True, "touch": True }
)
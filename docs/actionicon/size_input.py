import dash_mantine_components as dmc

component = dmc.Group([
    dmc.TextInput(placeholder="sm sixe input", size="sm"),
    dmc.ActionIcon(
        size="input-sm",
        variant="default",
        children="SM"
    )
])
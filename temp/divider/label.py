import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Divider(label="Click on update button to refresh"),
        dmc.Divider(label="Divider with centered content", labelPosition="center"),
        dmc.Divider(label="Divider with content on the right", labelPosition="right"),
    ],
)

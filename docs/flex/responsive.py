import dash_mantine_components as dmc

component = dmc.Flex(
    [
        dmc.Button("Button 1"),
        dmc.Button("Button 2"),
        dmc.Button("Button 3"),
    ],
    direction={"base": "column", "sm": "row"},
    gap={"base": "sm", "sm": "lg"},
    justify={"sm": "center"},
)

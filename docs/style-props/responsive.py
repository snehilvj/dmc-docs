import dash_mantine_components as dmc

component = dmc.Box(
    "Box with responsive style props",
    w={"base": 200, "sm": 400, "lg": 500},
    py={"base": "xs", "sm": "md", "lg": "xl"},
    bg={"base": "blue.7", "sm": "red.7", "lg": "green.7"},
    c="#fff",
    ta="center",
    mx="auto",
)

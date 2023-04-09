import dash_mantine_components as dmc

component = dmc.MantineProvider(
    theme={
        "colors": {
            "myColor": [
                "#EFF7A9",
                "#DEEA80",
                "#CCD962",
                "#C9DC2F",
                "#BCD113",
                "#ABBF02",
                "#9CB000",
                "#869800",
                "#728100",
            ]
        },
    },
    children=[dmc.Button("Custom Colors!", color="myColor")],
)

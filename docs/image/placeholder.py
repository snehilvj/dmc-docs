import dash_mantine_components as dmc

component = dmc.Group(
    position="apart",
    children=[
        dmc.Image(width=200, height=100, alt="Without placeholder"),
        dmc.Image(width=200, height=100, withPlaceholder=True),
        dmc.Image(
            width=200,
            height=100,
            withPlaceholder=True,
            placeholder="blah blah",
        ),
        dmc.Image(
            width=200,
            height=100,
            withPlaceholder=True,
            placeholder=[dmc.Loader(color="gray", size="sm")],
        ),
    ],
)
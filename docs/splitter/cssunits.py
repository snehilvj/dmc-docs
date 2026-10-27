import dash_mantine_components as dmc

component = dmc.Splitter(
    h=200,
    children=[
        dmc.SplitterPane(
            "Fixed 240px sidebar",
            defaultSize="240px",
            min="160px",
            max="50%",
            bg="blue",
        ),
        dmc.SplitterPane(
            "Flexible content",
            defaultSize=100,
            bg="teal",
        ),
    ],
)
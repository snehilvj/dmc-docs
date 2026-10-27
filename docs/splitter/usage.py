import dash_mantine_components as dmc

component = dmc.Splitter(
    h=200,
    classNames={"pane": "splitter-examples"},
    children=[
        dmc.SplitterPane(
            "First pane",
            defaultSize=50,
            min=20,
            bg="blue",
        ),
        dmc.SplitterPane(
            "Second pane",
            defaultSize=50,
            min=20,
            bg="teal",
        ),
    ],
)
import dash_mantine_components as dmc

component = dmc.Splitter(
    h=200,
    classNames={"pane": "splitter-examples"},
    children=[
        dmc.SplitterPane(
            "First",
            defaultSize=25,
            min=10,
            bg="blue",
        ),
        dmc.SplitterPane(
            "Second",
            defaultSize=50,
            min=10,
            bg="teal",
        ),
        dmc.SplitterPane(
            "Third",
            defaultSize=25,
            min=10,
            bg="grape",
        ),
    ],
)

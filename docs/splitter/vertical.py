import dash_mantine_components as dmc

component = dmc.Splitter(
    orientation="vertical",
    h=300,
    classNames={"pane": "splitter-examples"},
    children=[
        dmc.SplitterPane(
            "Top pane",
            defaultSize=60,
            min=20,
            bg="blue",
        ),
        dmc.SplitterPane(
            "Bottom pane",
            defaultSize=40,
            min=20,
            bg="teal",
        ),
    ],
)
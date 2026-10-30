import dash_mantine_components as dmc

component = dmc.Splitter(
    redistribute="nearest",
    h=200,
    classNames={"pane": "splitter-examples"},
    children=[
        dmc.SplitterPane(
            "Panel A",
            defaultSize=25,
            min=10,
            bg="blue",
        ),
        dmc.SplitterPane(
            "Panel B",
            defaultSize=25,
            min=10,
            bg="teal",
        ),
        dmc.SplitterPane(
            "Panel C",
            defaultSize=25,
            min=10,
            bg="grape",
        ),
        dmc.SplitterPane(
            "Panel D",
            defaultSize=25,
            min=10,
            bg="orange",
        ),
    ],
)
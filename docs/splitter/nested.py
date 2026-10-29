import dash_mantine_components as dmc

component = dmc.Splitter(
    h=350,
    children=[
        dmc.SplitterPane(
            "Sidebar",
            defaultSize=30,
            min=15,
            bg="blue",
            classNames={"pane": "splitter-examples"},
        ),
        dmc.SplitterPane(
            defaultSize=70,
            min=30,
            children=[
                dmc.Splitter(
                    orientation="vertical",
                    h="100%",
                    children=[
                        dmc.SplitterPane(
                            "Editor",
                            defaultSize=60,
                            min=20,
                            bg="teal",
                            classNames={"pane": "splitter-examples"},
                        ),
                        dmc.SplitterPane(
                            "Terminal",
                            defaultSize=40,
                            min=20,
                            bg="grape",
                            classNames={"pane": "splitter-examples"},
                        )
                    ]
                )
            ]
        )
    ],
)

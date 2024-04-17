import dash_mantine_components as dmc

component = dmc.List(
    [
        dmc.ListItem("First order item"),
        dmc.ListItem("First order item"),
        dmc.ListItem(
            [
                "First order item with list",
                dmc.List(
                    withPadding=True,
                    listStyleType="disc",
                    children=[
                        dmc.ListItem("Nested Item"),
                        dmc.ListItem("Nested Item"),
                        dmc.ListItem(
                            [
                                "Nested item with list",
                                dmc.List(
                                    withPadding=True,
                                    listStyleType="disc",
                                    children=[
                                        dmc.ListItem("Even more nested"),
                                        dmc.ListItem("Even more nested"),
                                    ],
                                ),
                            ]
                        ),
                        dmc.ListItem("Nested Item"),
                    ],
                ),
            ]
        ),
        dmc.ListItem("First order item"),
    ]
)

import dash_mantine_components as dmc

component = dmc.Box(
    style={"overflow": "hidden"},
    children=[
        dmc.Box(
            maw=500,
            p="md",
            mx="auto",
            bg="var(--mantine-color-blue-light)",
            children=[
                dmc.Text(
                    size="sm",
                    mb=5,
                    children=(
                        "preventGrowOverflow: true – each child width is always limited "
                        "to 33% of parent width (since there are 3 children)"
                    ),
                ),
                dmc.Group(
                    grow=True,
                    wrap="nowrap",
                    children=[
                        dmc.Button("First button", variant="default"),
                        dmc.Button("Second button with large content", variant="default"),
                        dmc.Button("Third button", variant="default"),
                    ],
                ),
                dmc.Text(
                    size="sm",
                    mb=5,
                    mt="md",
                    children=(
                        "preventGrowOverflow: false – children will grow based on their "
                        "content, they can take more than 33% of parent width"
                    ),
                ),
                dmc.Group(
                    grow=True,
                    preventGrowOverflow=False,
                    wrap="nowrap",
                    children=[
                        dmc.Button("First button", variant="default"),
                        dmc.Button("Second button with large content", variant="default"),
                        dmc.Button("Third button", variant="default"),
                    ],
                ),
            ],
        )
    ],
)

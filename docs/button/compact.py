import dash_mantine_components as dmc

sizes = ["xs", "sm", "md", "lg", "xl"]

component = dmc.Stack(
    [
        dmc.Group(
            [dmc.Button(f"Normal {size}", size=size) for size in sizes],
        ),
        dmc.Group(
            [dmc.Button(f"Compact {size}", size=f"compact-{size}") for size in sizes],
        ),
    ]
)

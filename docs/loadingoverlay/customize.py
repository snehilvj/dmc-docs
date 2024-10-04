import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.LoadingOverlay(
            loaderProps={"type": "bars", "color": "red", "size": "lg"},
            overlayProps={"radius": "sm", "blur": 2},
            visible=True,
            style={'zIndex': 10},
        ),
        dmc.BackgroundImage(
            dmc.Box(h=200, w=100),
            src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?ixlib=rb-1.2.1&ixid"
            "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=720&q=80",
        ),
    ],
    pos="relative",
)

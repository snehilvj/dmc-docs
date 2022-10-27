import dash_mantine_components as dmc

component = dmc.List(
    [
        dmc.ListItem(
            dmc.Text(
                [
                    "Join our ",
                    dmc.Anchor(
                        "Discord", href="https://discord.gg/KuJkh4Pyq5", underline=False
                    ),
                    " Community.",
                ]
            )
        ),
        dmc.ListItem("Install python virtual environment."),
    ]
)

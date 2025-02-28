import dash_mantine_components as dmc

component = dmc.Text(
    [
        "NASA’s ",
        dmc.Tooltip(
            dmc.Mark("JWST"),
            label="James Webb Space Telescope",
            boxWrapperProps={"style": {"display": "inline-block"}},
        ),
        " is the most powerful space telescope ever built.",
    ],
    span=True,
)

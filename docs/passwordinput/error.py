import dash_mantine_components as dmc


component = dmc.Group(
    [
        dmc.PasswordInput(
            placeholder="Your password",
            style={"width": 200},
            error=True,
        ),
        dmc.PasswordInput(
            placeholder="Your password", style={"width": 200}, error="Invalid Password"
        ),
    ],
    direction="column",
    position="center",
)

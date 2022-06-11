import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.PasswordInput(
            label="Disabled without value",
            placeholder="Your password",
            style={"width": 200},
            disabled=True,
        ),
        dmc.PasswordInput(
            label="Disabled with value",
            value="Password",
            disabled=True,
            style={"width": 200},
        ),
    ],
    direction="column",
    position="center",
)

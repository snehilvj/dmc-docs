import dash_mantine_components as dmc

component = dmc.Fieldset(
    children=[
        dmc.TextInput(label="Your name", placeholder="Your name"),
        dmc.TextInput(label="Email", placeholder="Email"),
        dmc.Group(
            [
                dmc.Button('Send')
            ],
            justify='flex-end'
        )
    ],
    legend="Personal information",
    disabled = True
)
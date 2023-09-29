import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.Textarea(label="Your message", style={"width": 500}, error=True),
        dmc.Textarea(
            label="Your message", style={"width": 500}, error="Message can't be empty!"
        ),
    ],
)

import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.Textarea(label="Your message", w=500, error=True),
        dmc.Textarea(label="Your message", w=500, error="Message can't be empty!"),
    ],
)

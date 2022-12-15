import dash_mantine_components as dmc

message = "Something happened! You made a mistake and there is no going back!"

component = dmc.Stack(
    children=[
        dmc.Alert(message, title="Primary", color="blue"),
        dmc.Alert(message, title="Secondary", color="gray"),
        dmc.Alert(message, title="Success!", color="green"),
        dmc.Alert(message, title="Warning!", color="yellow"),
        dmc.Alert(message, title="Danger!", color="red"),
        dmc.Alert(message, title="Info", color="violet"),
    ],
)

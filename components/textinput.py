import dash_mantine_components as dmc
from dash import html
from utils import create_component_title


textinput = html.Div(
    [
        create_component_title("TextInput"),
        dmc.Group(
            [
                dmc.TextInput(
                    value="snehilvj",
                    label="Username",
                    description="This is a description",
                    placeholder="username",
                ),
                dmc.TextInput(
                    value="why so curious",
                    label="Password",
                    description="Enter password",
                    placeholder="password",
                    type="password",
                ),
            ]
        ),
        dmc.Space(h=30),
    ]
)

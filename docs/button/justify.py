import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

icon = DashIconify(icon="tabler:photo", width=14)

component = dmc.Stack(
    [
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            rightSection=icon,
            variant="default",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            variant="default",
            mt="md",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            rightSection=icon,
            variant="default",
            mt="md",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=html.Span(),  # Empty spacer
            rightSection=icon,
            variant="default",
            mt="md",
        ),
    ]
)
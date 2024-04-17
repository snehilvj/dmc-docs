import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Stack(
    [
        dmc.ColorInput(
            label="Without preview",
            withPreview=False,
            value="#40c057",
            w=250,
        ),
        dmc.ColorInput(
            label="With icon",
            leftSection=DashIconify(icon="cil:paint"),
            withPreview=False,
            w=250,
            value="#40c057",
        ),
    ]
)

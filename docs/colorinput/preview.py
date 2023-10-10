import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Stack(
    [
        dmc.ColorInput(
            label="Without preview",
            withPreview=False,
            value="#40c057",
        ),
        dmc.ColorInput(
            label="With icon",
            icon=DashIconify(icon="cil:paint"),
            withPreview=False,
            value="#40c057",
        ),
    ]
)


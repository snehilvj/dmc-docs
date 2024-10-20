import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.ActionIcon([
    DashIconify(icon="mdi:heart-outline"),
    dmc.VisuallyHidden("Like post")
], variant="outline")

import dash_mantine_components as dmc
from .data import events

component = dmc.Box(
    dmc.Schedule(events=events, layout="responsive"),
    style={
        "resize": "horizontal",
        "overflow": "auto",
        "minWidth": 300,
        "maxWidth": "100%",
        "border": "2px dashed var(--mantine-color-blue-5)",
        "borderRadius": 8,
        "padding": 8,
    },
)
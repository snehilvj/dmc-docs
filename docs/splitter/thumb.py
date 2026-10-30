import dash_mantine_components as dmc
from dash_iconify import DashIconify

from docs.checkbox import iconcolor

component = dmc.Splitter(
    h=200,
    classNames={"pane": "splitter-examples"},
    handleIcon=DashIconify(icon="fa7-solid:grip-lines-vertical"),
    styles={
        "handle": {"backgroundColor": "var(--mantine-color-red-filled)"},
        "thumb": {
            "backgroundColor": "var(--mantine-color-green-filled)",
            "color": "var(--mantine-color-white)"
        },
    },
    bd="1px solid var(--mantine-color-default-border)",
    children=[
        dmc.SplitterPane(
            "First pane",
            defaultSize=50,
            min=20,
        ),
        dmc.SplitterPane(
            "Second pane",
            defaultSize=50,
            min=20,
        ),
    ],
)
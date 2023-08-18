import dash_mantine_components as dmc
from dash import html, Output, Input

component = dmc.HoverCard(
    withArrow=True,
    width=200,
    shadow="md",
    children=[
        dmc.HoverCardTarget(dmc.Button("Hover to reveal the card")),
        dmc.HoverCardDropdown(
            dmc.Text(
                "Hover card is revealed when user hovers over target element, it will be hidden once mouse is not over",
                size="sm",
            )
        ),
    ],
)

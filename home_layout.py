import dash_mantine_components as dmc
from dash import html

from reusable_components import ComponentName, OnlyCodeBlock, Title, OnlyComponentBlock

home_layout = html.Div(
    [
        ComponentName("Getting Started"),
        dmc.Space(h=20),
        dmc.Title("Installation", order=5, class_name="space-below-10"),
        OnlyCodeBlock("pip install dash_mantine_components"),
        dmc.Space(h=20),
        Title("Basic Usage"),
        OnlyCodeBlock(
            """from dash import Dash
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = dmc.Container([
    dmc.Alert(
        [
            "Hi from Dash Mantine Components. Please support us on",
            dmc.Anchor(
                "GitHub",
                href="https://github.com/snehilvj/dash-mantine-components",
                style={"marginLeft": 5},
                size="sm",
            ),
            "."
        ],
        title="Welcome!",
    )
])


if __name__ == "__main__":
    app.run_server()"""
        ),
        OnlyComponentBlock(
            dmc.Alert(
                [
                    "Hi from Dash Mantine Components. Please support us on",
                    dmc.Anchor(
                        "GitHub",
                        href="https://github.com/snehilvj/dash-mantine-components",
                        style={"marginLeft": 5},
                        size="sm",
                    ),
                    ".",
                ],
                title="Welcome!",
                color="violet",
            )
        ),
        dmc.Space(h=100),
    ]
)

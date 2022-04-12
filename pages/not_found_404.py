import dash
import dash_mantine_components as dmc

dash.register_page(__name__, path="/404")

layout = dmc.Group(
    direction="column",
    align="center",
    children=[
        dmc.Text("404", color="indigo", style={"fontSize": 40}),
        dmc.Text(
            [
                "If you think this page should exist, create an issue ",
                dmc.Anchor(
                    "here",
                    underline=False,
                    href="https://github.com/snehilvj/dash-mantine-components/issues/new",
                ),
                ".",
            ]
        ),
        dmc.Anchor("Go back to home ->", href="/", underline=False),
    ],
)

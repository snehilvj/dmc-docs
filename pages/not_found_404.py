import dash
import dash_mantine_components as dmc

from lib.constants import PAGE_TITLE_SUFFIX

dash.register_page(__name__, title="404" + PAGE_TITLE_SUFFIX, path="/404")

layout = dmc.Stack(
    align="center",
    children=[
        dmc.Text(
            [
                "If you think this page should exist, create an issue ",
                dmc.Anchor(
                    "here",
                    underline="never",
                    target="_blank",
                    href="https://github.com/snehilvj/dmc-docs/issues/new",
                ),
                ".",
            ]
        ),
        dmc.Anchor("Go back to home ->", href="/", underline="never"),
    ],
    mt=100,
)

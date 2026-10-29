import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Box(
    dmc.Anchor(
        href="https://mantine.dev",
        target="_blank",
        children=dmc.Center(
            [
                DashIconify(
                    icon="tabler:arrow-left",  # Use the Tabler Arrow Left icon
                    width=12,
                    height=12,
                ),
                dmc.Box("Back to Mantine website", ml=5),
            ],
            inline=True,
        ),
    )
)
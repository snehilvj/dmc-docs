import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group([
    dmc.CopyButton(
        value="https://www.dash-mantine-components.com/",
        children="Copy URL",
        copiedChildren="Copied!",
        color="blue",
        copiedColor="teal"
    ),
    dmc.CopyButton(
        value="This text is copied",
        children=DashIconify(icon="tabler:clipboard"),
        copiedChildren=DashIconify(icon="tabler:check"),
        color="blue",
        copiedColor="teal"
    ),
    dmc.CopyButton(
        value="This text is copied",
        children=DashIconify(icon="fa-regular:copy"),
        copiedChildren=DashIconify(icon="fa-regular:check-circle"),
        color="blue",
        copiedColor="teal",
    )
])

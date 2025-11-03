
import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.Group([
    dmc.Textarea(
        "Type here.  This text will be copied.",
        id="text-to-copy",
        autosize=True,
        minRows=3,
        w=300
    ),
    dmc.CopyButton(
        target_id="text-to-copy",
        children=DashIconify(icon="fa-regular:copy"),
        copiedChildren=DashIconify(icon="fa-regular:check-circle"),
        color="blue",
        copiedColor="teal",
        variant="outline",
        size="xs"
    )
], gap=0, align="flex-start" )

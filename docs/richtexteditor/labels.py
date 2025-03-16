import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.RichTextEditor(
    html="Custom button labels",
    extensions=[
        "StarterKit",
        "Underline",
        "Highlight",
    ],
    toolbar={
        "sticky": True,
        "controlsGroups": [
            [
                "Bold",
                "Italic",
                "Underline",
                "Strikethrough",
                "ClearFormatting",
                "Highlight",
                "Code",
            ],
        ],
    },
    labels={
        "boldControlLabel": "Make text bold",
        "italicControlLabel": "Make text bold",
        # ...other labels
    },
)

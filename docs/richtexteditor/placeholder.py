from dash import html
import dash_mantine_components as dmc

component = dmc.RichTextEditor(
    extensions=[
        "StarterKit",
        {"Placeholder": {"placeholder": "Write something..."}},
    ],
)

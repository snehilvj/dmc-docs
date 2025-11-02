import dash_mantine_components as dmc

component = dmc.RichTextEditor(
    html="Subtle rich text editor variant",
    extensions=[
        "StarterKit",
        "Highlight",
    ],
    toolbar={
        "sticky": True,
        "stickyOffset": 60,
        "variant": "subtle",
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
)

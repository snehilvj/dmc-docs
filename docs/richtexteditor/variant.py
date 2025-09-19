import dash_mantine_components as dmc

component = dmc.RichTextEditor(
    variant = "subtle",
    html="Subtle rich text editor variant",
    extensions=[
        "StarterKit",
        "Underline",
        "Highlight",
    ],
    toolbar={
        "sticky": True,
        "stickyOffset": 60,
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

import dash_mantine_components as dmc


content= '<p>Source code control example</p><p>New line with <strong>bold text</strong></p><p>New line with <em>italic</em> <em>text</em></p>'

component =dmc.RichTextEditor(
    html=content,
    toolbar={
        "sticky": True,
        "controlsGroups": [
            ["SourceCode"],
            [
                "Blockquote",
                "Bold",
                "Italic",
                "Underline",
                "Strikethrough",
                "ClearFormatting",
                "Highlight",
            ],
        ],
    },
)

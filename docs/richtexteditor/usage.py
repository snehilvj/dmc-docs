import dash_mantine_components as dmc

content = """<h2 style="text-align: center;">Welcome to Mantine rich text editor</h2><p><code>RichTextEditor</code> component focuses on usability and is designed to be as simple as possible to bring a familiar editing experience to regular users. <code>RichTextEditor</code> is based on <a href="https://tiptap.dev/" rel="noopener noreferrer" target="_blank">Tiptap.dev</a> and supports all of its features:</p><ul><li>General text formatting: <strong>bold</strong>, <em>italic</em>, <u>underline</u>, <s>strike-through</s> </li><li>Headings (h1-h6)</li><li>Sub and super scripts (<sup>&lt;sup /&gt;</sup> and <sub>&lt;sub /&gt;</sub> tags)</li><li>Ordered and bullet lists</li><li>Text align&nbsp;</li><li>And all <a href="https://tiptap.dev/extensions" target="_blank" rel="noopener noreferrer">other extensions</a></li></ul>"""

component = dmc.RichTextEditor(
    html=content,
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
            ["H1", "H2", "H3", "H4"],
            [
                "Blockquote",
                "Hr",
                "BulletList",
                "OrderedList",
                "Subscript",
                "Superscript",
            ],
            ["Link", "Unlink"],
            ["AlignLeft", "AlignCenter", "AlignJustify", "AlignRight"],
            ["Undo", "Redo"],
        ],
    },
)

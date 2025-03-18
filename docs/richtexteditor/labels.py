import dash_mantine_components as dmc


colorpicker_colors = [
    "#25262b",
    "#868e96",
    "#fa5252",
    "#e64980",
    "#be4bdb",
    "#7950f2",
    "#4c6ef5",
]

component = dmc.RichTextEditor(
    html="Custom button labels",
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
            [{"ColorPicker": {"colors": colorpicker_colors}}],
            [
                {"Color": {"color": "red"}},
                {"Color": {"color": "green"}},
                {"Color": {"color": "blue"}},
            ],
            ["UnsetColor"],
        ],
    },
    labels={
        "boldControlLabel": "Make text bold",
        "italicControlLabel": "Make text bold",
        "colorPickerControlLabel": "Text color", # label for control in toolbar
        "colorPickerColorLabel": "Color number: {color}", # include color in label in the color swatch. Use f-string format
        "colorControlLabel": "Set Text color {color}" # include color in label with f-string format
        # ...other labels
    },
)

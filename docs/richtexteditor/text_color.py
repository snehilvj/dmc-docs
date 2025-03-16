import dash_mantine_components as dmc

colorpicker_colors = [
    "#25262b",
    "#868e96",
    "#fa5252",
    "#e64980",
    "#be4bdb",
    "#7950f2",
    "#4c6ef5",
    "#228be6",
    "#15aabf",
    "#12b886",
    "#40c057",
    "#82c91e",
    "#fab005",
    "#fd7e14",
]

component = dmc.RichTextEditor(
    html="Apply some colors to this text",
    extensions=[
        "StarterKit",
        "Color",
        "TextStyle",  # required when using Color
    ],
    toolbar={
        "sticky": True,
        "stickyOffset": 60,
        "controlsGroups": [
            [
                {"ColorPicker": {"colors": colorpicker_colors}},
            ],
            [
                {"Color": {"color": "red"}},
                {"Color": {"color": "green"}},
                {"Color": {"color": "blue"}},
            ],
            ["UnsetColor"],
        ],
    },
)

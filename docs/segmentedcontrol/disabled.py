import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Text("Disabled control"),
        dmc.SegmentedControl(
            disabled=True,
            data=[
                {"value": "preview", "label": "Preview"},
                {"value": "code", "label": "Code"},
                {"value": "export", "label": "Export"},
            ],
        ),
        dmc.Text("Disabled option"),
        dmc.SegmentedControl(
            data=[
                {"value": "preview", "label": "Preview", "disabled": True},
                {"value": "code", "label": "Code"},
                {"value": "export", "label": "Export"},
            ],
        ),
    ],
    align="flex-start",
)

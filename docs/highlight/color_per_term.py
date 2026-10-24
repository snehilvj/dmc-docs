import dash_mantine_components as dmc

component = dmc.Highlight(
    "Error: Invalid input. Warning: Check this field. Success: All tests passed.",
    highlight=[
        {"text": "error", "color": "red"},
        {"text": "warning", "color": "yellow"},
        {"text": "success", "color": "green"},
    ],
)
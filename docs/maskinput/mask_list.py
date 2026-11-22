import dash_mantine_components as dmc

component = dmc.MaskInput(
    label="Time (HH:MM)",
    placeholder="__:__",
    mask=[
        {"regex": "[0-2]"},
        {"regex": r"\d"},
        ":",
        {"regex": "[0-5]"},
        {"regex": r"\d"},
    ],
)

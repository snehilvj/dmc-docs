import dash_mantine_components as dmc

component = dmc.MaskInput(
    label="Time (HH:MM)",
    placeholder="__:__",
    mask={"function": "timeMask"},
)
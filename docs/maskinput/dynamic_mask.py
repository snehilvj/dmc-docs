import dash_mantine_components as dmc

component = dmc.MaskInput(
    label="Credit card",
    placeholder="____ ____ ____ ____",
    mask="9999 9999 9999 9999",
    modify={"function": "creditCardMask"},
)
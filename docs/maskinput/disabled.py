import dash_mantine_components as dmc

component = dmc.MaskInput(
    label="Disabled Input",
    w=200,
    disabled=True,
    mask="99/99/9999",
    placeholder="mm/dd/yyyy"
)


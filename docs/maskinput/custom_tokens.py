import dash_mantine_components as dmc

component = dmc.MaskInput(
      label="Hex color",
      placeholder="#______",
      mask="\#hhhhhh",
      tokens={ "h": "[0-9a-fA-F]"}
)
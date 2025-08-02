
import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Autocomplete(
    label="Select with renderOption",
    placeholder="Select text align",
    data=[
      { "value": 'left', "label": 'Left' },
      { "value": 'center', "label": 'Center' },
      { "value": 'right', "label": 'Right' },
      { "value": 'justify', "label": 'Justify' },
    ],
    renderOption={"function": "renderOptionSelect"},
    clearable=True
)

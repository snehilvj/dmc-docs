
import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Autocomplete(
    label="Select with renderOption",
    placeholder="Select text align",
    data=[
      { "value": 'left', "label": 'left' },
      { "value": 'center', "label": 'center' },
      { "value": 'right', "label": 'right' },
      { "value": 'justify', "label": 'justify' },
    ],
    renderOption={"function": "renderOptionSelect"},
    clearable=True
)

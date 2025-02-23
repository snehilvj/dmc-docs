
import dash_mantine_components as dmc

component = dmc.Group([
    dmc.CheckboxIndicator(),
    dmc.CheckboxIndicator(checked=True),
    dmc.CheckboxIndicator(disabled=True),
    dmc.CheckboxIndicator(disabled=True, checked=True)
])

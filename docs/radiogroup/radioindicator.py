
import dash_mantine_components as dmc

component = dmc.Group([
    dmc.RadioIndicator(),
    dmc.RadioIndicator(checked=True),
    dmc.RadioIndicator(disabled=True),
    dmc.RadioIndicator(disabled=True, checked=True)
])

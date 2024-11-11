import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.Checkbox(checked=False, label="Default checkbox"),
    dmc.Checkbox(checked=False, indeterminate=True, label="Indeterminate checkbox"),
    dmc.Checkbox(checked=True, label="Checked checkbox"),
    dmc.Checkbox(checked=True, variant="outline", label="Outline checked checkbox"),
    dmc.Checkbox(variant="outline", indeterminate=True, label="Outline indeterminate checkbox"),
    dmc.Checkbox(disabled=True, label="Disabled checkbox"),
    dmc.Checkbox(disabled=True, checked=True, label="Disabled checked checkbox"),
    dmc.Checkbox(disabled=True, indeterminate=True, label="Disabled indeterminate checkbox")
])
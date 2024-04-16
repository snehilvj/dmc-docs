import dash_mantine_components as dmc

component = dmc.Checkbox(
    id="checkbox-simple",
    label=dmc.Text(
        ["I accept the ", dmc.Anchor("Terms and Conditions", href="#"), "."]
    ),
)

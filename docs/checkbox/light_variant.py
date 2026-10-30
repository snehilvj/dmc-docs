import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Checkbox(
            variant="light",
            checked=True,
            label="Light checkbox",
        ),
        dmc.Checkbox(
            variant="light",
            indeterminate=True,
            label="Light indeterminate checkbox",
        ),
        dmc.Checkbox(
            variant="light",
            color="teal",
            checked=True,
            label="Teal light checkbox",
        ),
        dmc.Checkbox(
            variant="light",
            color="grape",
            checked=True,
            label="Grape light checkbox",
        ),
        dmc.Checkbox(
            variant="light",
            color="#e64980",
            checked=True,
            label="Light checkbox with CSS color",
        ),
    ],
    gap=7,
)


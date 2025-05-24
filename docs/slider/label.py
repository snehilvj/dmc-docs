import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Text("No label", size="sm"),
        dmc.Slider(value=40, label=None),
        dmc.Text("Label always visible", size="sm", mt="xl"),
        dmc.Slider(value=40, labelAlwaysOn=True),
        dmc.Text("Custom label transition", size="sm", mt="xl"),
        dmc.Slider(
            value=40,
            labelTransitionProps={
                "transition": "skew-down",
                "duration": 150,
                "timingFunction": "linear",
            },
        ),
    ]
)



import dash_mantine_components as dmc

component = dmc.MantineProvider([
    dmc.Text("No label", size="sm"),
    dmc.Slider(value=40, label=None),

    dmc.Text("Formatted label", size="sm", mt="xl"),
    dmc.Slider(
        value=40,
        label={"function": "celsiusLabel"}
    ),

    dmc.Text("Label always visible", size="sm", mt="xl"),
    dmc.Slider(value=40, labelAlwaysOn=True),

    dmc.Text("Custom label transition", size="sm", mt="xl"),
    dmc.Slider(
        value=40,
        labelTransitionProps={
            "transition": "skew-down",
            "duration": 150,
            "timingFunction": "linear"
        }
    ),
])



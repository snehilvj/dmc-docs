import dash_mantine_components as dmc
from dash import html


def MantineThemeColorSwatches(id, value="#228ae6"):
    return dmc.ColorPicker(
        id=id,
        value=value,
        withPicker=False,
        swatchesPerRow=7,
        swatches=[
            "#25262b",
            "#868e96",
            "#fa5252",
            "#e64980",
            "#be4bdb",
            "#7950f2",
            "#4c6ef5",
            "#228ae6",
            "#15abbf",
            "#12b886",
            "#3fbf57",
            "#82c91e",
            "#fab005",
            "#fc7d14",
        ],
    )


def DemoSelect(id, value, label, data):
    return dmc.Select(
        id=id,
        value=value,
        label=label,
        searchable=False,
        clearable=False,
        data=[
            {
                "label": val.title(),
                "value": val,
            }
            for val in data
        ],
    )


def DemoSlider(id, label, initial_value):
    return dmc.InputWrapper(
        label=label,
        children=[
            html.Div(
                [
                    dmc.Slider(
                        id=id,
                        value=initial_value,
                        marks=[
                            {"value": 1},
                            {"value": 2},
                            {"value": 3},
                            {"value": 4},
                            {"value": 5},
                        ],
                        min=1,
                        max=5,
                        size="sm",
                    )
                ],
                style={"padding": "0 5px"},
            )
        ],
    )


def DemoSegmentedControl(id, label, values, initial_value):
    return dmc.InputWrapper(
        label=label,
        children=[
            html.Div(
                [
                    dmc.SegmentedControl(
                        id=id,
                        fullWidth=True,
                        value=initial_value,
                        data=[{"label": val, "value": val.lower()} for val in values],
                    )
                ],
            )
        ],
    )

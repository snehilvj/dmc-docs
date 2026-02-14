import dash_mantine_components as dmc
from dash import dcc

component = dmc.Card([
    dmc.SimpleGrid(
        [
            dmc.InputWrapper(
                dcc.Dropdown([f"option {i}" for i in range(100)],  value=["option 1", "option 2", "option 3"], multi=True, id="dcc-dropdown"),
                label="dcc.Dropdown",
                htmlFor="dcc-dropdown"
            ),
            dmc.NumberInput(
                label="dmc.NumberInput",
                value=30712,
                thousandSeparator=True,
                prefix="$ ",

            ),
            dmc.DatePickerInput(label="dmc.DatePickerInput", value="2025-12-05"),
        ],
        cols={"base": 1, "md": 3},
    ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="dmc"  # applies Mantine styles
)

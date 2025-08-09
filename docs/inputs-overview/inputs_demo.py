
import dash_mantine_components as dmc

input_props = {}


component = dmc.Card([
    dmc.SimpleGrid(
        cols=3,
        spacing="xs",
        verticalSpacing=25,
        children=[
            dmc.TextInput(
                label="TextInput",
                placeholder="Text input",
                **input_props
            ),
            dmc.NumberInput(
                label="NumberInput",
                placeholder="Number input",
                value=30712,
                thousandSeparator=True,
                prefix="$ ",
                **input_props
            ),
            dmc.DatePickerInput(
                label="Date range picker",
                placeholder="Your last vacation",
                type="range",
                popoverProps={"radius": "md"},
                **input_props
            ),
            dmc.TimePicker(label="TimePicker"),
            dmc.MonthPickerInput(label="MonthPicker"),
            dmc.ColorInput(
                label="Color input",
                value="#129ce0",
                placeholder="What other library has color input?",
                format="rgba",
                popoverProps={"radius": "md"},
                **input_props
            ),
            dmc.PasswordInput(
                label="PasswordInput",
                placeholder="Secret",
                value="😎🤏🤨🕶️🤏",
                **input_props
            ),
            dmc.Select(
                label="Select",
                placeholder="Pick one option",
                data=[
                    "🇩🇪 Germany",
                    "🇫🇷 France",
                    "🇬🇧 United Kingdom",
                    "🇺🇸 United States of America"
                ],
                value="🇫🇷 France",
                checkIconPosition="right",
                **input_props
            ),
            dmc.MultiSelect(
                label="MultiSelect",
                data=["A", "B", "C", "D", "E", "F"],
                value=["A", "C"],
                comboboxProps={"radius": "md"},
                **input_props
            ),
        ]
    )
], withBorder=True)

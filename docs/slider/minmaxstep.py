
import dash_mantine_components as dmc

marks = [
    {"value": 0, "label": "xs"},
    {"value": 25, "label": "sm"},
    {"value": 50, "label": "md"},
    {"value": 75, "label": "lg"},
    {"value": 100, "label": "xl"},
]

component = dmc.Container([
    dmc.Text("Decimal step"),
    dmc.Slider(
        value=0,
        min=-10,
        max=10,
        step=0.1,
        label={"function": "formatDecimal"},
        styles={"markLabel": {"display": "none"}},
    ),

    dmc.Text("Step matched with marks", mt="md"),
    dmc.Slider(
        value=50,
        step=25,
        marks=marks,
        label={"function": "labelFromMarks", "options": {"marks": marks}},
        styles={"markLabel": {"display": "none"}},
    ),
], p="xl")

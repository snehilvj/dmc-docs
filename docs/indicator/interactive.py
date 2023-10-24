import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components.configurator import Configurator

TARGET_ID = "indicator-interactive"

target = dmc.Center(
    dmc.Indicator(
        dmc.Avatar(
            DashIconify(icon="fluent:mail-48-filled", height=75), variant="outline"
        ),
        id=TARGET_ID,
    )
)

configurator = Configurator(target, TARGET_ID)
configurator.add_colorpicker("color", "indigo")
configurator.add_select(
    "position",
    [
        "bottom-end",
        "bottom-start",
        "top-end",
        "top-start",
        "bottom-center",
        "top-center",
        "middle-center",
        "middle-end",
        "middle-start",
    ],
    "top-end",
)
configurator.add_text_input("label", "4")
configurator.add_number_input("size", 15)
configurator.add_number_input("offset", 0)
configurator.add_slider("radius", "xl")
configurator.add_switch("processing", False)
configurator.add_switch("withBorder", False)
configurator.add_switch("disabled", False)

component = configurator.panel

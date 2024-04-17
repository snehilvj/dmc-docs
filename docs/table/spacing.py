import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Table(
    data={
        "caption": "Some elements from periodic table",
        "head": ["Element position", "Atomic mass", "Symbol", "Element name"],
        "body": [
            [6, 12.011, "C", "Carbon"],
            [7, 14.007, "N", "Nitrogen"],
            [39, 88.906, "Y", "Yttrium"],
            [56, 137.33, "Ba", "Barium"],
            [58, 140.12, "Ce", "Cerium"],
        ],
    }
)

configurator = Configurator(target)
configurator.add_slider("horizontalSpacing", "xs")
configurator.add_slider("verticalSpacing", "xs")

component = configurator.panel

import dash_mantine_components as dmc

component = dmc.Table(
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

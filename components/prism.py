from dash import html
import dash_mantine_components as dmc
from utils import create_component_title

code = """class DumbMaths:
    def __init__(self) -> None:
        self.res = 0

    def add(a: int, b: int):
        return 0

    def mult(a: int, b: int):
        return 0
"""


prism = html.Div(
    [
        create_component_title("Prism"),
        dmc.SimpleGrid(
            cols=2,
            children=[
                dmc.Prism(
                    language="python",
                    code=code,
                ),
                dmc.Prism(
                    colorScheme="dark",
                    language="python",
                    code=code,
                ),
            ],
        ),
        dmc.Space(h=30),
    ]
)

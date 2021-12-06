from dash import html
import dash_mantine_components as dmc
from utils import create_component_title

text = html.Div(
    [
        create_component_title("Text"),
        dmc.Text(
            "From Bulbapedia: Bulbasaur is a small, quadrupedal Pokémon that has blue-green skin with darker patches. It has red eyes with white pupils, pointed, ear-like structures on top of its head, and a short, blunt snout with a wide mouth. A pair of small, pointed teeth are visible in the upper jaw when its mouth is open. Each of its thick legs ends with three sharp claws. On Bulbasaur's back is a green plant bulb, which is grown from a seed planted there at birth. The bulb also conceals two slender, tentacle-like vines and provides",
            variant="gradient",
            gradient={"from": "indigo", "to": "red", "deg": 45},
            size="xl",
            lineClamp=4,
        ),
        dmc.Space(h=30),
    ]
)

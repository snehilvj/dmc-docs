
import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data

component = dmc.Tree(
    data=data,
    withLines=True,
    levelOffset=40,
    expanded=[
        "node_modules",
        "node_modules/@mantine",
        "node_modules/@mantine/form",
        "node_modules/@mantine/form/index.d.ts",
    ],
)

import pandas as pd
from dash import html
import dash_mantine_components as dmc
from utils import create_component_title

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

table = html.Div(
    [
        create_component_title("Table"),
        dmc.Table(
            id="table",
            striped=True,
            highlightOnHover=True,
            rows=df.values.tolist(),
            columns=df.columns,
        ),
        dmc.Space(h=30),
    ]
)

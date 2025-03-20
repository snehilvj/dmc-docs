
from dash import  html
import dash_mantine_components as dmc
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

component = html.Div(
    [
        html.Div([
            html.H4("Example without TypographyStylesProvider"),
            generate_table(df),
        ], style={"marginBottom": 36}),

        dmc.TypographyStylesProvider([
            html.H4("Example with TypographyStylesProvider"),
            generate_table(df),
        ]),
    ]
)

import random

import dash_mantine_components as dmc
import pandas as pd
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
from dash import html, dcc


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table


def create_figure():
    return go.Figure(
        {
            "data": [
                go.Bar(
                    x=list(range(10)),
                    y=[random.randint(200, 1000) for _ in range(10)],
                    name="SF",
                    marker={"line": {"width": 0}},
                    marker_color=dmc.theme.DEFAULT_COLORS["gray"][4],
                ),
                go.Bar(
                    x=list(range(10)),
                    y=[random.randint(200, 1000) for _ in range(10)],
                    name="Montréal",
                    marker={"line": {"width": 0}},
                    marker_color=dmc.theme.DEFAULT_COLORS["indigo"][4],
                ),
            ],
            "layout": go.Layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis={"showgrid": False, "zeroline": False, "visible": False},
                yaxis={"showgrid": False, "zeroline": False, "visible": False},
                showlegend=False,
            ),
        }
    )


def create_graph():
    return dcc.Graph(figure=create_figure(), config={"displayModeBar": False})


def create_styles_api_table(category, component):
    url = f"https://v6.mantine.dev/{category}/{component}/?t=styles-api"

    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    dataframes = []
    df = pd.DataFrame()
    for table in tables:
        headers = []
        for th in table.find_all("th"):
            headers.append(th.text.strip())
        rows = []
        for tr in table.find_all("tr"):
            row = []
            for td in tr.find_all("td"):
                row.append(td.text.strip())
            if row:
                rows.append(row)
        print(rows, headers)
        df = pd.DataFrame(rows, columns=headers)
        dataframes.append(df)
    markdown_table = df.to_markdown(index=False)
    return markdown_table

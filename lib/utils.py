import random

import dash_mantine_components as dmc
import pandas as pd
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
from dash import dcc
from dash import html
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])

session.mount("http://", HTTPAdapter(max_retries=retries))
session.mount("https://", HTTPAdapter(max_retries=retries))


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


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table


def create_styles_api_table(category, component):
    url = f"https://v5.mantine.dev/{category}/{component}/?t=styles-api"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    dataframes = []
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
        df = pd.DataFrame(rows, columns=headers)
        dataframes.append(df)

    layout = []
    for df in dataframes:
        if "Static selector" in df.columns:
            layout.append(dmc.Table(create_table(df), withBorder=True, mb=20))
    return layout


exclude_prop_names = [
    "unstyled",
    "bg",
    "bgp",
    "bgr",
    "bgsz",
    "bottom",
    "c",
    "display",
    "ff",
    "fs",
    "fw",
    "fz",
    "h",
    "w",
    "inset",
    "left",
    "lh",
    "lts",
    "m",
    "mah",
    "maw",
    "mb",
    "mih",
    "miw",
    "ml",
    "mr",
    "mt",
    "mx",
    "my",
    "opacity",
    "p",
    "pb",
    "pl",
    "pos",
    "pr",
    "pt",
    "px",
    "py",
    "right",
    "ta",
    "td",
    "top",
    "tt",
]

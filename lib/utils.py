import random

import dash_mantine_components as dmc
import pandas as pd
import plotly.graph_objects as go
import requests
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


def get_styles_api_dict(component):
    url = f"https://raw.githubusercontent.com/mantinedev/mantine/master/src/mantine-styles-api/src/styles-api/{component}.styles-api.ts"
    req = session.get(url)
    data = req.text.split("\n")
    while True:
        line = data.pop(0)
        if "export" in line:
            data.pop(-2)
            break
    d = {}
    for e in data:
        if ":" in e:
            name, desc = e.split(":")
            d[name.strip()] = desc.lstrip(" '").rstrip("',")
        elif e.strip().startswith("..."):
            comp = e.strip().strip("...").rstrip(",")
            d.update(**get_styles_api_dict(comp))
    return d


def create_styles_api_table(component):
    styles = get_styles_api_dict(component)
    df = pd.DataFrame(styles.items(), columns=["Name", "Description"])
    df["Static Selector"] = f".mantine-{component}-" + df["Name"]
    df = df[["Name", "Static Selector", "Description"]]
    return dmc.Table(create_table(df), withBorder=True, mb=20)


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

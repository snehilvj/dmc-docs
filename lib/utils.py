import random

import dash_mantine_components as dmc
import pandas as pd
import requests
from bs4 import BeautifulSoup


def create_table(df):
    columns, values = df.columns, df.values
    header = [dmc.TableTr([dmc.TableTh(col) for col in columns])]
    rows = [dmc.TableTr([dmc.TableTd(cell) for cell in row]) for row in values]
    table = [dmc.TableThead(header), dmc.TableTbody(rows)]
    return table


def create_graph():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
    ]
    data = [
        {
            "month": month,
            "Smartphones": random.randint(700, 1800),
            "Laptops": random.randint(100, 1000),
            "Tablets": random.randint(200,600),
            "Watches": random.randint(200, 1800),
        }
        for month in months
    ]

    return dmc.BarChart(
        h=500,
        data=data,
        dataKey="month",
        series=[
            {"name": "Smartphones", "color": "violet.6"},
            {"name": "Laptops", "color": "blue.6"},
            {"name": "Tablets", "color": "teal.6"},
            {"name": "Watches", "color": "indigo.6"},
        ],
        tickLine="y",
    )


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

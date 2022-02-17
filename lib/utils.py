import random

from dash import html, dcc


def render_html_table(columns, rows):
    html_header = [html.Tr([html.Th(col) for col in columns])]
    html_rows = [html.Tr([html.Td(children=cell) for cell in row]) for row in rows]
    html_table = [html.Thead(html_header), html.Tbody(html_rows)]
    return html_table


def create_figure():
    return {
        "data": [
            {
                "x": list(range(10)),
                "y": [random.randint(200, 1000) for _ in range(10)],
                "type": "bar",
                "name": "SF",
            },
            {
                "x": list(range(10)),
                "y": [random.randint(200, 1000) for _ in range(10)],
                "type": "bar",
                "name": u"Montréal",
            },
        ]
    }


def create_graph():
    return dcc.Graph(figure=create_figure())

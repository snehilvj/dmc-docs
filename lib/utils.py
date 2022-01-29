from dash import html


def render_html_table(columns, rows):
    html_header = [html.Tr([html.Th(col) for col in columns])]
    html_rows = [html.Tr([html.Td(children=cell) for cell in row]) for row in rows]
    html_table = [html.Thead(html_header), html.Tbody(html_rows)]
    return html_table

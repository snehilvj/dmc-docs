# dash-ag-grid >= 33.3.3
import dash_ag_grid as dag
from dash import clientside_callback, Input, Output, html
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")

theme =  {
    "function": (
        "themeQuartz.withParams({"        
        "accentColor: 'var(--mantine-primary-color-filled)', "
        "fontFamily: 'var(--mantine-font-family)', "
        "headerFontWeight: 'bold'"
        "})"
    )
}

component = html.Div([
    dag.AgGrid(
        id="theme-color-scheme33",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in ["athlete", "country", "sport", "year"]],
        defaultColDef={"flex": 1, "filter": True},
        dashGridOptions={
            "theme": theme,
            "rowSelection": {"mode": "multiRow"}
        },
    ),
    html.Div(id="dummy-output")
])


clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-ag-theme-mode', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update;        
    }
    """,
    Output("dummy-output", "children"),
    Input("docs-color-scheme-switch", "checked"),
)



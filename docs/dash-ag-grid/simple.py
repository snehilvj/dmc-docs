import dash_ag_grid as dag
import pandas as pd
from dash import callback, Input, Output

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

component = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    id="dag-simple"
)

@callback(
    Output("dag-simple", "className"),
    Input("docs-color-scheme-switch", "computedColorScheme")
)
def update_theme(color):
    return "ag-theme-alpine-dark" if color=="dark" else "ag-theme-alpine"
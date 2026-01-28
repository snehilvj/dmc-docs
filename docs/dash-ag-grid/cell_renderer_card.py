
from dash import callback, Input, Output
import dash_ag_grid as dag
import pandas as pd

data = {
    "stats": ["Revenue", "EBITDA", "Net Income"],
    "results": ['$13,120,000','$1,117,000', '$788,000'],
    "change": [10.1, -22.1, 18.6],
    'comments': ['Enter your comments here...', '', '']
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "",
        "cellRenderer": "DMC_Card",
    },
    {
        "field": "comments",
        "editable": True,
        "cellEditorPopup": True,
        "cellEditor": "agLargeTextCellEditor",
        "flex": 1
    },
]

component = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    dashGridOptions={"rowHeight": 120},
    id="dag-dmc-card-grid",
)


@callback(
    Output("dag-dmc-card-grid", "className"),
    Input("docs-color-scheme-switch", "computedColorScheme")
)
def update_theme(color):
    return "ag-theme-alpine-dark" if color=="dark" else "ag-theme-alpine"



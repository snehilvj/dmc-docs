# dash-ag-grid >= 33.3.3
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")

theme =  {
    "function": (
        "themeQuartz.withParams({"        
           "backgroundColor: 'var(--mantine-color-body)', "
           "foregroundColor: 'var(--mantine-color-text)', "
        "})"
    )
}

component = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in ["athlete", "country", "sport", "year"]],
    defaultColDef={"flex": 1, "filter": True},
    dashGridOptions={
        "theme": theme,
        "rowSelection": {"mode": "multiRow"}
    },
)


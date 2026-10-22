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

# Theme switch in the dmc-docs header:
# dmc.ColorSchemeToggle(
#     lightIcon=DashIconify(icon="radix-icons:sun", width=20),
#     darkIcon=DashIconify(icon="radix-icons:moon", width=20),
#     variant="light",
#     color="gray",
#     id="docs-color-scheme-switch",
# )

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
])


clientside_callback(
    """
    (colorScheme) => {
        document.documentElement.setAttribute(
            'data-ag-theme-mode',
            colorScheme
        );
        return window.dash_clientside.no_update;
    }
    """,
    Input("docs-color-scheme-switch", "computedColorScheme"),
)

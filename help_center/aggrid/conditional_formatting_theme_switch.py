"""
Example of
- styling dash-ag-grid for light and dark mantine themes
- using dmc function `light-dark` to set different colors based on theme
- using mantine css variables to set grid style
"""


import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output, clientside_callback, callback
from dash_iconify import DashIconify
import dash_ag_grid as dag
import pandas as pd
_dash_renderer._set_react_version("18.2.0")

def make_grid():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    athlete_cellStyle = {
        'backgroundColor': 'light-dark(var(--mantine-color-gray-1), var(--mantine-color-gray-7)',
        'fontWeight' : 700
    }

    total_cellStyle = {
        "styleConditions": [
            {
                "condition": "params.value >= 6",
                "style": {"backgroundColor": "var(--mantine-color-yellow-filled)"},
            },
        ]
    }

    columnDefs = [
        {"field": "athlete",  'cellStyle': athlete_cellStyle},
        {"field": "sport" },
        {"field": "year" },
        {"field": "total", 'cellStyle': total_cellStyle},
    ]

    return  dag.AgGrid(
        id="grid",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="sizeToFit",
        dashGridOptions={"animateRows": False},
    )


theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color= "var(--mantine-color-yellow-8)"),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color= "var(--mantine-color-yellow-6)"),
    id="color-scheme-switch",
    persistence=True,
    color="grey",
)

app = Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    dmc.Box([
        dmc.Group([
            dmc.Title("Dash AG Grid with theme switch"),
            theme_toggle
        ], pb="md"),
        make_grid()
    ], m="lg")
)


clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-switch", "id"),
    Input("color-scheme-switch", "checked"),
)


@callback(
    Output("grid", "className"),
    Input("color-scheme-switch", "checked"),
)
def update_grid_theme(switch_on):
    if switch_on:
        return "ag-theme-alpine-dark"
    return "ag-theme-alpine"


if __name__ == "__main__":
    app.run(debug=True)
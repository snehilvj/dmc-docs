"""
Example from https://py.cafe/BSd3v./dash-ag-grid-mantine-app

How to use DMC as cell editors in Dash Ag Grid
"""

import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")
import dash_ag_grid as dag
import pandas as pd

app = Dash(__name__, external_stylesheets=dmc.styles.ALL)

now = "2024-12-30"

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5, 6],
    'DatePickerInput': [now, now, now, now, now, now],
    'TagsInput': [['A']] * 6,  # Note TagsInput values must be a list
    'Select': ['A', 'B', 'C', 'A', 'B', 'C']
})

columnDefs = [
    { "field": "Column 1"},
    {
        "field": "DatePickerInput",
        'cellEditor': {'function': 'AllFunctionalComponentEditors'},
        'cellEditorParams': {'component': dmc.DatePickerInput(valueFormat="YYYY-MM-DD")},
        'cellEditorPopup': True,
    },
    {
        "field": "TagsInput",
        'cellEditor': {'function': 'AllFunctionalComponentEditors'},
        'cellEditorParams': {'component': dmc.TagsInput(data=["A", "B", "C"])},
        'cellEditorPopup': True,
    },
    {
        "field": "Select",
        'cellEditor': {'function': 'AllFunctionalComponentEditors'},
        'cellEditorParams': {'component': dmc.Select(data=["A", "B", "C"])},
        'cellEditorPopup': True,
    },
]


component = dmc.Box([
    dmc.Title('Dash AG Grid with DMC components as cell editors', order=3),
    dag.AgGrid(
        id='grid_id',
        columnDefs=columnDefs,
        columnSize="autoSize",
        rowData=df.to_dict('records'),
        defaultColDef={'editable': True},
        className="ag-theme-alpine-dark",
    ),
], p="lg")


app.layout = dmc.MantineProvider(
    component,
    forceColorScheme="dark"
)

if __name__ == "__main__":
    app.run(debug=True)

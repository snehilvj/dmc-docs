from dash import callback, Input, Output
import dash_mantine_components as dmc
import dash_ag_grid as dag
import pandas as pd

now = "2025-12-30"

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


component = dag.AgGrid(
    id='dag-dmc-cell-editor',
    columnDefs=columnDefs,
    columnSize="autoSize",
    rowData=df.to_dict('records'),
    defaultColDef={'editable': True},
    dashGridOptions={'singleClickEdit': True}
)


@callback(
    Output("dag-dmc-cell-editor", "className"),
    Input("docs-color-scheme-switch", "checked")
)
def update_theme(switch_on):
    return "ag-theme-alpine-dark" if switch_on else "ag-theme-alpine"


import dash_mantine_components as dmc

from dash import Input, Output, callback


component =  dmc.InputWrapper(
    id="tree-wrapper",
    label="Tree input",
    description="This is a tree input",
    inputWrapperOrder=["label", "description", "error", "input"],
    withAsterisk=True,
    children=[
        dmc.Tree(
            id="tree",
            checkboxes=True,
            data=[
                {
                    "label": "root",
                    "value": "value",
                    "children": [
                        {"label": "child 1", "value": "child_1"},
                        {"label": "child 2", "value": "child_2"},
                    ],
                }
            ],
        )
    ],
)

@callback(
    Output("tree-wrapper", "error"),
    Input("tree", "checked"),
)
def validate(checked):
    tree_error = "Select at least one" if not checked else None
    return tree_error


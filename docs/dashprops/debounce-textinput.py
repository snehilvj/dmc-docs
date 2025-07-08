import dash_mantine_components as dmc
from dash import  callback, Input, Output

component = dmc.Stack(

    [
        dmc.TextInput(
            id="debounce-text",
            label="Enter your comments",
            debounce=True
        ),
        dmc.Text(id="debounce-text-output"),
    ],
)


@callback(
    Output("debounce-text-output", "children"),
    Input("debounce-text", "value"),
)
def update_output(comments):
    if not comments:
        return ""
    return f"Thank you for your feedback: {comments}"

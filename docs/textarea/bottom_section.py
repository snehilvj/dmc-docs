import dash_mantine_components as dmc
from dash import  Input, Output, clientside_callback

component = dmc.Textarea(
    id="textarea-bottom-section",
    autosize=True,
    minRows=3,
    label="Message",
    bottomSection=dmc.Text(
        id="char-count",
        size="xs",
        c="dimmed",
    ),
)

clientside_callback(
    """
    function(value) {
        const length = (value || "").length;
        return `${length}/500 characters`;
    }
    """,
    Output("char-count", "children"),
    Input("textarea-bottom-section", "value"),
)
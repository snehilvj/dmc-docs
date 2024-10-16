import dash_mantine_components as dmc

component = dmc.Tooltip(
    label="tooltip label",
    children=dmc.Textarea(
        value="How to set the width of the textarea with a tooltip to 100%", w="100%"
    ),
    boxWrapperProps={"w": "100%"},
)

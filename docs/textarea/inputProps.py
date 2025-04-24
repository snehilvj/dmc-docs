import dash_mantine_components as dmc

component = dmc.Textarea(
    inputProps={"maxLength": 3},
    label="Enter text",
    description="Max length of 3 characters",
)


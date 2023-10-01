import dash_mantine_components as dmc

component = dmc.JsonInput(
    label="Your json data",
    placeholder="This component will auto-size to fit the content.",
    validationError="Invalid json",
    formatOnBlur=True,
    autosize=True,
    minRows=4,
)

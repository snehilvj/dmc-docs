import dash_mantine_components as dmc

component = dmc.JsonInput(
    label="Your package.json",
    placeholder="Textarea will autosize to fit the content",
    validationError="Invalid JSON",
    formatOnBlur=True,
    autosize=True,
    minRows=4,
)

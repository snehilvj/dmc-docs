import dash_mantine_components as dmc

component = dmc.CopyButton(
    value="copied text",
    children="Copy",
    copiedChildren="Copied",
    color="dark.3",
    copiedColor="gray.2",
    autoContrast=True,
    timeout="2000"
)

import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.CodeHighlight(
        code = "dmc.Text('This codeblock has a custom copy button label')",
        language="python",
        copyLabel="Copy button code",
        copiedLabel="Copied!",
    ),
    dmc.CodeHighlight(
            code = "dmc.Text('This codeblock does not have a copy button')",
            language="python",
            withCopyButton=False,
            mt="md"
        )
])
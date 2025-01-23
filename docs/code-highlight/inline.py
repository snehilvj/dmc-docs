import dash_mantine_components as dmc

component = dmc.Text(
    [
        "You can highlight code inline ",
        dmc.InlineCodeHighlight(
            code='dmc.InlineCodeHighlight(code="Your code string here", language="python")',
            language="python",
        ),
        " Is not that cool?",
    ]
)

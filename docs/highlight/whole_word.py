import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Text(
        "With whole word matching (wholeWord=True)",
        size="sm", c="dimmed",
    ),
    dmc.Highlight(
        "The theme is there",
        highlight="the",
        wholeWord=True,
    ),
    dmc.Text(
        "Without whole word matching (default)",
        size="sm", c="dimmed", mt="lg",
    ),
    dmc.Highlight(
        "The theme is there",
        highlight="the",

    ),
])

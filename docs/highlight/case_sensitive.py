import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Text(
        "With case-insensitive matching (default)",
        size="sm", c="dimmed",
    ),
    dmc.Highlight(
        "Highlight This, definitely THIS and also this!",
        highlight="this",
    ),
    dmc.Text(
        "With case-sensitive matching (caseInsensitive=False)",
        size="sm", c="dimmed", mt="lg",
    ),
    dmc.Highlight(
        "Highlight This, definitely THIS and also this!",
        highlight="this",
        caseInsensitive=False,
    ),
])
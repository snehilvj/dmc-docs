import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Text(
        "With accent-insensitive matching (default)",
        size="sm", c="dimmed",
    ),
    dmc.Highlight(
        "We visited café and cafe.",
         highlight="cafe",
    ),
    dmc.Text(
        "With accent-sensitive matching (accentInsensitive=False)",
        size="sm", c="dimmed", mt="lg",
    ),
    dmc.Highlight(
        "We visited café and cafe.",
        highlight="cafe",
        accentInsensitive=False,
    ),
])
